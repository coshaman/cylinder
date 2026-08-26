#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

#ifdef _WIN32
#include <windows.h>
#else
#include <sys/resource.h>
#endif

namespace {

using Value = std::int64_t;
constexpr Value kInfinity = std::numeric_limits<Value>::max();
constexpr std::uint64_t kRuntimeCapSeconds = 30U * 60U;
constexpr std::uint64_t kRamCapBytes = 8ULL * 1024ULL * 1024ULL * 1024ULL;

struct Edge {
    std::size_t tail;
    std::size_t head;
    Value weight;
};

struct Matrix {
    std::size_t size;
    std::vector<Value> values;

    explicit Matrix(std::size_t dimension)
        : size(dimension), values(dimension * dimension, kInfinity) {}

    Value& at(std::size_t row, std::size_t column) {
        return values[row * size + column];
    }

    const Value& at(std::size_t row, std::size_t column) const {
        return values[row * size + column];
    }
};

struct Manifest {
    int width;
    std::size_t state_count;
    std::size_t transition_count;
    std::string sha256;
    std::vector<Edge> edges;
};

std::uint32_t rotate_right(std::uint32_t value, std::uint32_t bits) {
    return (value >> bits) | (value << (32U - bits));
}

std::string sha256_bytes(const std::string& input) {
    static constexpr std::array<std::uint32_t, 64> k = {
        0x428a2f98U, 0x71374491U, 0xb5c0fbcfU, 0xe9b5dba5U, 0x3956c25bU, 0x59f111f1U, 0x923f82a4U, 0xab1c5ed5U,
        0xd807aa98U, 0x12835b01U, 0x243185beU, 0x550c7dc3U, 0x72be5d74U, 0x80deb1feU, 0x9bdc06a7U, 0xc19bf174U,
        0xe49b69c1U, 0xefbe4786U, 0x0fc19dc6U, 0x240ca1ccU, 0x2de92c6fU, 0x4a7484aaU, 0x5cb0a9dcU, 0x76f988daU,
        0x983e5152U, 0xa831c66dU, 0xb00327c8U, 0xbf597fc7U, 0xc6e00bf3U, 0xd5a79147U, 0x06ca6351U, 0x14292967U,
        0x27b70a85U, 0x2e1b2138U, 0x4d2c6dfcU, 0x53380d13U, 0x650a7354U, 0x766a0abbU, 0x81c2c92eU, 0x92722c85U,
        0xa2bfe8a1U, 0xa81a664bU, 0xc24b8b70U, 0xc76c51a3U, 0xd192e819U, 0xd6990624U, 0xf40e3585U, 0x106aa070U,
        0x19a4c116U, 0x1e376c08U, 0x2748774cU, 0x34b0bcb5U, 0x391c0cb3U, 0x4ed8aa4aU, 0x5b9cca4fU, 0x682e6ff3U,
        0x748f82eeU, 0x78a5636fU, 0x84c87814U, 0x8cc70208U, 0x90befffaU, 0xa4506cebU, 0xbef9a3f7U, 0xc67178f2U,
    };
    std::vector<std::uint8_t> bytes(input.begin(), input.end());
    const std::uint64_t bit_length = static_cast<std::uint64_t>(bytes.size()) * 8U;
    bytes.push_back(0x80U);
    while ((bytes.size() % 64U) != 56U) {
        bytes.push_back(0U);
    }
    for (int shift = 56; shift >= 0; shift -= 8) {
        bytes.push_back(static_cast<std::uint8_t>((bit_length >> shift) & 0xffU));
    }

    std::array<std::uint32_t, 8> h = {
        0x6a09e667U, 0xbb67ae85U, 0x3c6ef372U, 0xa54ff53aU,
        0x510e527fU, 0x9b05688cU, 0x1f83d9abU, 0x5be0cd19U,
    };
    for (std::size_t offset = 0; offset < bytes.size(); offset += 64U) {
        std::array<std::uint32_t, 64> w{};
        for (int i = 0; i < 16; ++i) {
            const std::size_t j = offset + static_cast<std::size_t>(i) * 4U;
            w[i] = (static_cast<std::uint32_t>(bytes[j]) << 24) |
                   (static_cast<std::uint32_t>(bytes[j + 1]) << 16) |
                   (static_cast<std::uint32_t>(bytes[j + 2]) << 8) |
                   static_cast<std::uint32_t>(bytes[j + 3]);
        }
        for (int i = 16; i < 64; ++i) {
            const std::uint32_t s0 = rotate_right(w[i - 15], 7) ^ rotate_right(w[i - 15], 18) ^ (w[i - 15] >> 3);
            const std::uint32_t s1 = rotate_right(w[i - 2], 17) ^ rotate_right(w[i - 2], 19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16] + s0 + w[i - 7] + s1;
        }
        std::uint32_t a = h[0], b = h[1], c = h[2], d = h[3];
        std::uint32_t e = h[4], f = h[5], g = h[6], current = h[7];
        for (int i = 0; i < 64; ++i) {
            const std::uint32_t s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25);
            const std::uint32_t choose = (e & f) ^ ((~e) & g);
            const std::uint32_t temp1 = current + s1 + choose + k[i] + w[i];
            const std::uint32_t s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22);
            const std::uint32_t majority = (a & b) ^ (a & c) ^ (b & c);
            const std::uint32_t temp2 = s0 + majority;
            current = g; g = f; f = e; e = d + temp1; d = c; c = b; b = a; a = temp1 + temp2;
        }
        h[0] += a; h[1] += b; h[2] += c; h[3] += d;
        h[4] += e; h[5] += f; h[6] += g; h[7] += current;
    }
    std::ostringstream output;
    for (std::uint32_t word : h) {
        output << std::hex << std::setfill('0') << std::setw(8) << word;
    }
    return output.str();
}

std::string sha256_file(const std::filesystem::path& path) {
    std::ifstream input(path, std::ios::binary);
    if (!input) {
        throw std::runtime_error("cannot read file for SHA-256: " + path.string());
    }
    std::ostringstream bytes;
    bytes << input.rdbuf();
    return sha256_bytes(bytes.str());
}

std::size_t parse_number_after(const std::string& text, const std::string& key, std::size_t start = 0) {
    const std::size_t marker = text.find(key, start);
    if (marker == std::string::npos) {
        throw std::runtime_error("manifest is missing " + key);
    }
    std::size_t cursor = marker + key.size();
    while (cursor < text.size() && (text[cursor] == ' ' || text[cursor] == '\t' || text[cursor] == '\r' || text[cursor] == '\n')) {
        ++cursor;
    }
    std::size_t end = cursor;
    while (end < text.size() && text[end] >= '0' && text[end] <= '9') {
        ++end;
    }
    if (end == cursor) {
        throw std::runtime_error("manifest has a non-integer " + key);
    }
    return static_cast<std::size_t>(std::stoull(text.substr(cursor, end - cursor)));
}

std::vector<Edge> parse_edges(const std::string& text) {
    const std::string key = "\"transitions\":[";
    const std::size_t begin = text.find(key);
    if (begin == std::string::npos) {
        throw std::runtime_error("manifest is missing transitions");
    }
    std::size_t cursor = begin + key.size();
    // The persisted manifest places transitions last; use its final closing
    // bracket so every edge tuple is consumed.
    const std::size_t end = text.rfind(']');
    if (end == std::string::npos) {
        throw std::runtime_error("manifest transitions are unterminated");
    }
    std::vector<Edge> edges;
    while (cursor < end) {
        const std::size_t open = text.find('[', cursor);
        if (open == std::string::npos || open >= end) {
            break;
        }
        const std::size_t close = text.find(']', open);
        if (close == std::string::npos || close > end) {
            throw std::runtime_error("manifest transition is unterminated");
        }
        std::string tuple = text.substr(open + 1, close - open - 1);
        std::replace(tuple.begin(), tuple.end(), ',', ' ');
        std::istringstream values(tuple);
        std::size_t tail = 0, head = 0;
        Value weight = 0;
        if (!(values >> tail >> head >> weight)) {
            throw std::runtime_error("manifest contains an invalid transition");
        }
        edges.push_back({tail, head, weight});
        cursor = close + 1;
    }
    return edges;
}

Manifest read_manifest(const std::filesystem::path& path, int requested_width) {
    std::ifstream input(path);
    if (!input) {
        throw std::runtime_error("cannot read automaton manifest: " + path.string());
    }
    std::ostringstream contents;
    contents << input.rdbuf();
    const std::string text = contents.str();
    const std::size_t width = parse_number_after(text, "\"width\":");
    const std::size_t state_count = parse_number_after(text, "\"state_count\":");
    const std::size_t transition_count = parse_number_after(text, "\"transition_count\":");
    if (width != static_cast<std::size_t>(requested_width)) {
        throw std::runtime_error("manifest width does not match requested width");
    }
    std::vector<Edge> edges = parse_edges(text);
    if (edges.size() != transition_count) {
        throw std::runtime_error("manifest transition count does not match its edge list");
    }
    for (const Edge& edge : edges) {
        if (edge.tail >= state_count || edge.head >= state_count || edge.weight < 0) {
            throw std::runtime_error("manifest contains an out-of-range transition");
        }
    }
    return {requested_width, state_count, transition_count, sha256_file(path), std::move(edges)};
}

std::uint64_t peak_rss_bytes() {
#ifdef _WIN32
    using MemoryCounters = struct {
        DWORD cb;
        DWORD page_fault_count;
        SIZE_T peak_working_set_size;
        SIZE_T working_set_size;
        SIZE_T quota_peak_paged_pool_usage;
        SIZE_T quota_paged_pool_usage;
        SIZE_T quota_peak_non_paged_pool_usage;
        SIZE_T quota_non_paged_pool_usage;
        SIZE_T pagefile_usage;
        SIZE_T peak_pagefile_usage;
    };
    using QueryFn = BOOL(WINAPI*)(HANDLE, MemoryCounters*, DWORD);
    HMODULE module = LoadLibraryA("psapi.dll");
    if (module != nullptr) {
        const auto query = reinterpret_cast<QueryFn>(GetProcAddress(module, "GetProcessMemoryInfo"));
        if (query != nullptr) {
            MemoryCounters counters{};
            counters.cb = sizeof(counters);
            if (query(GetCurrentProcess(), &counters, sizeof(counters))) {
                FreeLibrary(module);
                return static_cast<std::uint64_t>(counters.peak_working_set_size);
            }
        }
        FreeLibrary(module);
    }
    return 0;
#else
    struct rusage usage{};
    if (getrusage(RUSAGE_SELF, &usage) == 0) {
        return static_cast<std::uint64_t>(usage.ru_maxrss) * 1024ULL;
    }
    return 0;
#endif
}

class ResourceMonitor {
public:
    ResourceMonitor()
        : started_(std::chrono::steady_clock::now()) {}

    void check() const {
        const auto elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - started_).count();
        if (elapsed > static_cast<double>(kRuntimeCapSeconds)) {
            throw std::runtime_error("30-minute runtime cap exceeded");
        }
        if (peak_rss_bytes() > kRamCapBytes) {
            throw std::runtime_error("8-GB RAM cap exceeded");
        }
    }

    double seconds() const {
        return std::chrono::duration<double>(std::chrono::steady_clock::now() - started_).count();
    }

private:
    std::chrono::steady_clock::time_point started_;
};

Matrix minplus_power(const Manifest& manifest, std::size_t exponent, const ResourceMonitor& monitor) {
    Matrix current(manifest.state_count);
    for (std::size_t state = 0; state < manifest.state_count; ++state) {
        current.at(state, state) = 0;
    }
    std::vector<std::vector<Edge>> outgoing(manifest.state_count);
    for (const Edge& edge : manifest.edges) {
        outgoing[edge.tail].push_back(edge);
    }

    for (std::size_t step = 0; step < exponent; ++step) {
        Matrix next(manifest.state_count);
        for (std::size_t row = 0; row < manifest.state_count; ++row) {
            const std::size_t row_offset = row * manifest.state_count;
            for (std::size_t tail = 0; tail < manifest.state_count; ++tail) {
                const Value prefix = current.values[row_offset + tail];
                if (prefix == kInfinity) {
                    continue;
                }
                for (const Edge& edge : outgoing[tail]) {
                    const Value candidate = prefix + edge.weight;
                    Value& destination = next.values[row_offset + edge.head];
                    if (candidate < destination) {
                        destination = candidate;
                    }
                }
            }
        }
        current = std::move(next);
        monitor.check();
    }
    return current;
}

void write_u32(std::ofstream& output, std::uint32_t value) {
    output.write(reinterpret_cast<const char*>(&value), sizeof(value));
}

void write_u64(std::ofstream& output, std::uint64_t value) {
    output.write(reinterpret_cast<const char*>(&value), sizeof(value));
}

void write_matrix(const Matrix& matrix, const std::filesystem::path& path) {
    std::ofstream output(path, std::ios::binary | std::ios::trunc);
    if (!output) {
        throw std::runtime_error("cannot write matrix: " + path.string());
    }
    output.write("MTX1", 4);
    write_u32(output, 1U);
    write_u64(output, static_cast<std::uint64_t>(matrix.size));
    for (Value value : matrix.values) {
        const std::uint8_t tag = value == kInfinity ? 0U : 1U;
        output.write(reinterpret_cast<const char*>(&tag), sizeof(tag));
        if (tag == 1U) {
            output.write(reinterpret_cast<const char*>(&value), sizeof(value));
        }
    }
    if (!output) {
        throw std::runtime_error("failed while writing matrix: " + path.string());
    }
}

struct Comparison {
    std::size_t mismatch_count = 0;
    std::size_t first_row = 0;
    std::size_t first_column = 0;
    Value first_left = kInfinity;
    Value first_right = kInfinity;
};

Comparison compare_shifted(const Matrix& base, const Matrix& shifted, Value scalar) {
    Comparison result;
    for (std::size_t row = 0; row < base.size; ++row) {
        for (std::size_t column = 0; column < base.size; ++column) {
            const Value left = base.at(row, column);
            const Value expected = left == kInfinity ? kInfinity : left + scalar;
            if (shifted.at(row, column) != expected) {
                if (result.mismatch_count == 0) {
                    result.first_row = row;
                    result.first_column = column;
                    result.first_left = expected;
                    result.first_right = shifted.at(row, column);
                }
                ++result.mismatch_count;
            }
        }
    }
    return result;
}

std::string entry_json(Value value) {
    return value == kInfinity ? "\"INF\"" : std::to_string(value);
}

void write_metadata(
    const std::filesystem::path& path,
    const Manifest& manifest,
    std::size_t n,
    std::size_t p,
    Value c,
    const Comparison& comparison,
    double runtime_seconds,
    std::uint64_t peak_rss,
    const std::filesystem::path& matrix_n,
    const std::filesystem::path& matrix_np) {
    const bool holds = comparison.mismatch_count == 0;
    std::ofstream output(path, std::ios::trunc);
    if (!output) {
        throw std::runtime_error("cannot write identity metadata: " + path.string());
    }
    output << "{\n"
           << "  \"width\": " << manifest.width << ",\n"
           << "  \"state_count\": " << manifest.state_count << ",\n"
           << "  \"transition_count\": " << manifest.transition_count << ",\n"
           << "  \"N\": " << n << ",\n"
           << "  \"p\": " << p << ",\n"
           << "  \"c\": " << c << ",\n"
           << "  \"matrix_format\": \"MTX1 little-endian uint64 dimension, tagged int64 entries\",\n"
           << "  \"status\": \"" << (holds ? "TOOL_CHECKED_LOCAL" : "PROTOTYPE_IDENTITY_NOT_REPRODUCED") << "\",\n"
           << "  \"identity_holds\": " << (holds ? "true" : "false") << ",\n"
           << "  \"mismatch_count\": " << comparison.mismatch_count << ",\n"
           << "  \"first_mismatch\": {\"row\": " << comparison.first_row
           << ", \"column\": " << comparison.first_column
           << ", \"expected\": " << entry_json(comparison.first_left)
           << ", \"actual\": " << entry_json(comparison.first_right) << "},\n"
           << "  \"manifest_sha256\": \"" << manifest.sha256 << "\",\n"
           << "  \"M_N_sha256\": \"" << sha256_file(matrix_n) << "\",\n"
           << "  \"M_N_plus_p_sha256\": \"" << sha256_file(matrix_np) << "\",\n"
           << "  \"runtime_seconds\": " << std::fixed << std::setprecision(6) << runtime_seconds << ",\n"
           << "  \"peak_rss_bytes\": " << peak_rss << ",\n"
           << "  \"runtime_cap_seconds\": " << kRuntimeCapSeconds << ",\n"
           << "  \"ram_cap_bytes\": " << kRamCapBytes << ",\n"
           << "  \"producer_command\": \"g++ -std=c++17 -O2 src/automaton/power_identity.cpp -o power_identity && power_identity width manifest output_dir\"\n"
           << "}\n";
}

struct Parameters {
    std::size_t n;
    std::size_t p;
    Value c;
};

Parameters parameters_for(int width) {
    switch (width) {
    case 5: return {16, 4, 6};
    case 6: return {21, 14, 24};
    case 7: return {28, 4, 8};
    default: throw std::invalid_argument("width must be 5, 6, or 7");
    }
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 4) {
        std::cerr << "usage: power_identity <width> <automaton_manifest.json> <output_dir>\n";
        return 2;
    }
    try {
        const int width = std::stoi(argv[1]);
        const Parameters parameters = parameters_for(width);
        const Manifest manifest = read_manifest(argv[2], width);
        const std::filesystem::path output_dir(argv[3]);
        std::filesystem::create_directories(output_dir);
        const ResourceMonitor monitor;

        const Matrix matrix_n = minplus_power(manifest, parameters.n, monitor);
        const Matrix matrix_np = minplus_power(manifest, parameters.n + parameters.p, monitor);
        const std::filesystem::path matrix_n_path = output_dir / "M_N.bin";
        const std::filesystem::path matrix_np_path = output_dir / "M_N_plus_p.bin";
        write_matrix(matrix_n, matrix_n_path);
        write_matrix(matrix_np, matrix_np_path);
        const Comparison comparison = compare_shifted(matrix_n, matrix_np, parameters.c);
        write_metadata(
            output_dir / "matrix_identity.json", manifest, parameters.n, parameters.p, parameters.c,
            comparison, monitor.seconds(), peak_rss_bytes(), matrix_n_path, matrix_np_path);

        std::cout << "width=" << width << " status="
                  << (comparison.mismatch_count == 0 ? "TOOL_CHECKED_LOCAL" : "PROTOTYPE_IDENTITY_NOT_REPRODUCED")
                  << " mismatches=" << comparison.mismatch_count
                  << " runtime_seconds=" << std::fixed << std::setprecision(6) << monitor.seconds()
                  << " peak_rss_bytes=" << peak_rss_bytes() << "\n";
        return 0;
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
