#include <array>
#include <cstdint>
#include <deque>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace automaton {

struct State {
    int selected;
    int pending;
};

struct Edge {
    int tail;
    int head;
    int weight;
};

std::vector<State> generate_states(int width);
std::vector<Edge> generate_transitions(int width);

namespace {

uint32_t rotate_right(uint32_t value, uint32_t bits) {
    return (value >> bits) | (value << (32 - bits));
}

std::string sha256(const std::string& input) {
    static constexpr std::array<uint32_t, 64> k = {
        0x428a2f98U, 0x71374491U, 0xb5c0fbcfU, 0xe9b5dba5U, 0x3956c25bU, 0x59f111f1U, 0x923f82a4U, 0xab1c5ed5U,
        0xd807aa98U, 0x12835b01U, 0x243185beU, 0x550c7dc3U, 0x72be5d74U, 0x80deb1feU, 0x9bdc06a7U, 0xc19bf174U,
        0xe49b69c1U, 0xefbe4786U, 0x0fc19dc6U, 0x240ca1ccU, 0x2de92c6fU, 0x4a7484aaU, 0x5cb0a9dcU, 0x76f988daU,
        0x983e5152U, 0xa831c66dU, 0xb00327c8U, 0xbf597fc7U, 0xc6e00bf3U, 0xd5a79147U, 0x06ca6351U, 0x14292967U,
        0x27b70a85U, 0x2e1b2138U, 0x4d2c6dfcU, 0x53380d13U, 0x650a7354U, 0x766a0abbU, 0x81c2c92eU, 0x92722c85U,
        0xa2bfe8a1U, 0xa81a664bU, 0xc24b8b70U, 0xc76c51a3U, 0xd192e819U, 0xd6990624U, 0xf40e3585U, 0x106aa070U,
        0x19a4c116U, 0x1e376c08U, 0x2748774cU, 0x34b0bcb5U, 0x391c0cb3U, 0x4ed8aa4aU, 0x5b9cca4fU, 0x682e6ff3U,
        0x748f82eeU, 0x78a5636fU, 0x84c87814U, 0x8cc70208U, 0x90befffaU, 0xa4506cebU, 0xbef9a3f7U, 0xc67178f2U,
    };

    std::vector<uint8_t> bytes(input.begin(), input.end());
    const uint64_t bit_length = static_cast<uint64_t>(bytes.size()) * 8U;
    bytes.push_back(0x80U);
    while ((bytes.size() % 64U) != 56U) {
        bytes.push_back(0U);
    }
    for (int shift = 56; shift >= 0; shift -= 8) {
        bytes.push_back(static_cast<uint8_t>((bit_length >> shift) & 0xffU));
    }

    uint32_t h0 = 0x6a09e667U;
    uint32_t h1 = 0xbb67ae85U;
    uint32_t h2 = 0x3c6ef372U;
    uint32_t h3 = 0xa54ff53aU;
    uint32_t h4 = 0x510e527fU;
    uint32_t h5 = 0x9b05688cU;
    uint32_t h6 = 0x1f83d9abU;
    uint32_t h7 = 0x5be0cd19U;

    for (size_t offset = 0; offset < bytes.size(); offset += 64) {
        std::array<uint32_t, 64> w{};
        for (int i = 0; i < 16; ++i) {
            const size_t j = offset + static_cast<size_t>(i) * 4U;
            w[i] = (static_cast<uint32_t>(bytes[j]) << 24) |
                   (static_cast<uint32_t>(bytes[j + 1]) << 16) |
                   (static_cast<uint32_t>(bytes[j + 2]) << 8) |
                   static_cast<uint32_t>(bytes[j + 3]);
        }
        for (int i = 16; i < 64; ++i) {
            const uint32_t s0 = rotate_right(w[i - 15], 7) ^ rotate_right(w[i - 15], 18) ^ (w[i - 15] >> 3);
            const uint32_t s1 = rotate_right(w[i - 2], 17) ^ rotate_right(w[i - 2], 19) ^ (w[i - 2] >> 10);
            w[i] = w[i - 16] + s0 + w[i - 7] + s1;
        }

        uint32_t a = h0;
        uint32_t b = h1;
        uint32_t c = h2;
        uint32_t d = h3;
        uint32_t e = h4;
        uint32_t f = h5;
        uint32_t g = h6;
        uint32_t h = h7;

        for (int i = 0; i < 64; ++i) {
            const uint32_t s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25);
            const uint32_t ch = (e & f) ^ ((~e) & g);
            const uint32_t temp1 = h + s1 + ch + k[i] + w[i];
            const uint32_t s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22);
            const uint32_t maj = (a & b) ^ (a & c) ^ (b & c);
            const uint32_t temp2 = s0 + maj;
            h = g;
            g = f;
            f = e;
            e = d + temp1;
            d = c;
            c = b;
            b = a;
            a = temp1 + temp2;
        }

        h0 += a;
        h1 += b;
        h2 += c;
        h3 += d;
        h4 += e;
        h5 += f;
        h6 += g;
        h7 += h;
    }

    std::ostringstream out;
    for (uint32_t word : {h0, h1, h2, h3, h4, h5, h6, h7}) {
        out << std::hex << std::setfill('0') << std::setw(8) << word;
    }
    return out.str();
}

std::string canonical_states(const std::vector<State>& states) {
    std::ostringstream out;
    for (const State& state : states) {
        out << state.selected << "," << state.pending << "\n";
    }
    return out.str();
}

std::string canonical_edges(const std::vector<Edge>& edges) {
    std::ostringstream out;
    for (const Edge& edge : edges) {
        out << edge.tail << "," << edge.head << "," << edge.weight << "\n";
    }
    return out.str();
}

std::vector<int> reachable_from(int start, const std::vector<std::vector<int>>& graph) {
    std::vector<int> seen(graph.size(), 0);
    std::deque<int> queue;
    seen[start] = 1;
    queue.push_back(start);

    while (!queue.empty()) {
        const int node = queue.front();
        queue.pop_front();
        for (int next : graph[node]) {
            if (seen[next] == 0) {
                seen[next] = 1;
                queue.push_back(next);
            }
        }
    }
    return seen;
}

bool strongly_connected(size_t state_count, const std::vector<Edge>& edges) {
    if (state_count == 0) {
        return true;
    }

    std::vector<std::vector<int>> forward(state_count);
    std::vector<std::vector<int>> reverse(state_count);
    for (const Edge& edge : edges) {
        forward[edge.tail].push_back(edge.head);
        reverse[edge.head].push_back(edge.tail);
    }

    for (int seen : reachable_from(0, forward)) {
        if (seen == 0) {
            return false;
        }
    }
    for (int seen : reachable_from(0, reverse)) {
        if (seen == 0) {
            return false;
        }
    }
    return true;
}

std::string producer_command(int width) {
    std::ostringstream out;
    out << "g++ -std=c++17 -O2 src/automaton/manifest.cpp src/automaton/states.cpp "
        << "src/automaton/transitions.cpp -o automaton_manifest && automaton_manifest "
        << width;
    return out.str();
}

void write_json(int width, const std::vector<State>& states, const std::vector<Edge>& edges) {
    std::cout << "{\n";
    std::cout << "\"width\":" << width << ",\n";
    std::cout << "\"state_count\":" << states.size() << ",\n";
    std::cout << "\"transition_count\":" << edges.size() << ",\n";
    std::cout << "\"state_sha256\":\"" << sha256(canonical_states(states)) << "\",\n";
    std::cout << "\"transition_sha256\":\"" << sha256(canonical_edges(edges)) << "\",\n";
    std::cout << "\"strongly_connected\":" << (strongly_connected(states.size(), edges) ? "true" : "false") << ",\n";
    std::cout << "\"producer_command\":\"" << producer_command(width) << "\",\n";
    std::cout << "\"states\":[";
    for (size_t i = 0; i < states.size(); ++i) {
        if (i != 0) {
            std::cout << ",";
        }
        std::cout << "[" << states[i].selected << "," << states[i].pending << "]";
    }
    std::cout << "],\n";
    std::cout << "\"transitions\":[";
    for (size_t i = 0; i < edges.size(); ++i) {
        if (i != 0) {
            std::cout << ",";
        }
        std::cout << "[" << edges[i].tail << "," << edges[i].head << "," << edges[i].weight << "]";
    }
    std::cout << "]\n";
    std::cout << "}\n";
}

}  // namespace

}  // namespace automaton

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: automaton_manifest <width>\n";
        return 2;
    }

    try {
        const int width = std::stoi(argv[1]);
        const std::vector<automaton::State> states = automaton::generate_states(width);
        const std::vector<automaton::Edge> edges = automaton::generate_transitions(width);
        automaton::write_json(width, states, edges);
    } catch (const std::exception& error) {
        std::cerr << error.what() << "\n";
        return 1;
    }
    return 0;
}
