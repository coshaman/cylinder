#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

// Clean-room verifier: this translation unit deliberately has no producer
// dependency or shared min-plus declaration.
namespace {

class BigInt {
public:
    explicit BigInt(long long value = 0)
        : BigInt(std::to_string(value)) {}

    explicit BigInt(const std::string& text) {
        if (text.empty()) {
            throw std::invalid_argument("empty integer");
        }
        std::size_t offset = 0;
        if (text[0] == '-' || text[0] == '+') {
            negative_ = text[0] == '-';
            offset = 1;
        }
        if (offset == text.size()) {
            throw std::invalid_argument("invalid integer");
        }
        for (std::size_t index = offset; index < text.size(); ++index) {
            if (text[index] < '0' || text[index] > '9') {
                throw std::invalid_argument("invalid integer");
            }
        }
        digits_ = text.substr(offset);
        trim();
    }

    friend BigInt operator+(const BigInt& left, const BigInt& right) {
        if (left.negative_ == right.negative_) {
            return make(left.negative_, sum(left.digits_, right.digits_));
        }
        const int order = absolute_compare(left.digits_, right.digits_);
        if (order == 0) {
            return BigInt(0);
        }
        return order > 0
            ? make(left.negative_, difference(left.digits_, right.digits_))
            : make(right.negative_, difference(right.digits_, left.digits_));
    }

    friend bool operator<(const BigInt& left, const BigInt& right) {
        if (left.negative_ != right.negative_) {
            return left.negative_;
        }
        const int order = absolute_compare(left.digits_, right.digits_);
        return left.negative_ ? order > 0 : order < 0;
    }

    friend std::ostream& operator<<(std::ostream& output, const BigInt& value) {
        if (value.negative_ && value.digits_ != "0") {
            output << '-';
        }
        return output << value.digits_;
    }

private:
    bool negative_ = false;
    std::string digits_ = "0";

    static int absolute_compare(const std::string& left, const std::string& right) {
        if (left.size() != right.size()) {
            return left.size() < right.size() ? -1 : 1;
        }
        if (left == right) {
            return 0;
        }
        return left < right ? -1 : 1;
    }

    static std::string sum(const std::string& left, const std::string& right) {
        std::string result;
        int carry = 0;
        std::size_t first = left.size();
        std::size_t second = right.size();
        while (first || second || carry) {
            const int a = first ? left[--first] - '0' : 0;
            const int b = second ? right[--second] - '0' : 0;
            const int total = a + b + carry;
            result.push_back(static_cast<char>('0' + total % 10));
            carry = total / 10;
        }
        std::reverse(result.begin(), result.end());
        return result;
    }

    static std::string difference(const std::string& larger, const std::string& smaller) {
        std::string result;
        int borrow = 0;
        std::size_t first = larger.size();
        std::size_t second = smaller.size();
        while (first) {
            int digit = larger[--first] - '0' - borrow;
            if (second) {
                digit -= smaller[--second] - '0';
            }
            if (digit < 0) {
                digit += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
            result.push_back(static_cast<char>('0' + digit));
        }
        std::reverse(result.begin(), result.end());
        const std::size_t first_nonzero = result.find_first_not_of('0');
        return first_nonzero == std::string::npos ? "0" : result.substr(first_nonzero);
    }

    static BigInt make(bool negative, std::string digits) {
        BigInt result;
        result.negative_ = negative;
        result.digits_ = std::move(digits);
        result.trim();
        return result;
    }

    void trim() {
        const std::size_t first = digits_.find_first_not_of('0');
        digits_ = first == std::string::npos ? "0" : digits_.substr(first);
        if (digits_ == "0") {
            negative_ = false;
        }
    }
};

struct Cost {
    bool reachable = false;
    BigInt value = BigInt(0);
};

struct Grid {
    std::size_t side;
    std::vector<Cost> cells;

    explicit Grid(std::size_t size) : side(size), cells(checked_size(size)) {}

    static std::size_t checked_size(std::size_t size) {
        if (size != 0 && size > std::numeric_limits<std::size_t>::max() / size) {
            throw std::length_error("matrix dimensions overflow");
        }
        return size * size;
    }

    Cost& at(std::size_t row, std::size_t column) {
        return cells[row * side + column];
    }

    const Cost& at(std::size_t row, std::size_t column) const {
        return cells[row * side + column];
    }
};

Cost extend(const Cost& first, const Cost& second) {
    if (!first.reachable || !second.reachable) {
        return Cost{};
    }
    return {true, first.value + second.value};
}

Grid independently_multiply(const Grid& left, const Grid& right) {
    if (left.side != right.side) {
        throw std::invalid_argument("independent verifier dimension mismatch");
    }
    Grid result(left.side);
    for (std::size_t row = 0; row < left.side; ++row) {
        for (std::size_t middle = 0; middle < left.side; ++middle) {
            for (std::size_t column = 0; column < left.side; ++column) {
                const Cost candidate = extend(left.at(row, middle), right.at(middle, column));
                if (candidate.reachable &&
                    (!result.at(row, column).reachable ||
                     candidate.value < result.at(row, column).value)) {
                    result.at(row, column) = candidate;
                }
            }
        }
    }
    return result;
}

Grid identity(std::size_t size) {
    Grid result(size);
    for (std::size_t index = 0; index < size; ++index) {
        result.at(index, index) = Cost{true, BigInt(0)};
    }
    return result;
}

Grid independently_power(const Grid& base, std::uint64_t exponent) {
    Grid result = identity(base.side);
    Grid repeated = base;
    while (exponent > 0) {
        if (exponent % 2 == 1) {
            result = independently_multiply(result, repeated);
        }
        exponent /= 2;
        if (exponent > 0) {
            repeated = independently_multiply(repeated, repeated);
        }
    }
    return result;
}

Cost minimum_diagonal(const Grid& matrix) {
    Cost result;
    for (std::size_t index = 0; index < matrix.side; ++index) {
        const Cost& candidate = matrix.at(index, index);
        if (candidate.reachable &&
            (!result.reachable || candidate.value < result.value)) {
            result = candidate;
        }
    }
    return result;
}

Cost parse_cost(const std::string& token) {
    if (token == "INF") {
        return Cost{};
    }
    return Cost{true, BigInt(token)};
}

Grid read_grid(std::istream& input, std::size_t size) {
    Grid matrix(size);
    std::string token;
    for (Cost& cell : matrix.cells) {
        if (!(input >> token)) {
            throw std::invalid_argument("missing matrix entry");
        }
        cell = parse_cost(token);
    }
    return matrix;
}

void print_cost(const Cost& cost) {
    if (cost.reachable) {
        std::cout << cost.value;
    } else {
        std::cout << "INF";
    }
}

void print_grid(const Grid& matrix) {
    std::cout << matrix.side << ' ' << matrix.side;
    for (const Cost& cell : matrix.cells) {
        std::cout << ' ';
        print_cost(cell);
    }
    std::cout << '\n';
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: independent_minplus {multiply|power|diagonal}\n";
        return 2;
    }

    try {
        const std::string operation = argv[1];
        std::size_t size = 0;
        if (!(std::cin >> size)) {
            throw std::invalid_argument("missing matrix size");
        }
        if (operation == "multiply") {
            const Grid left = read_grid(std::cin, size);
            const Grid right = read_grid(std::cin, size);
            print_grid(independently_multiply(left, right));
        } else if (operation == "power") {
            std::uint64_t exponent = 0;
            if (!(std::cin >> exponent)) {
                throw std::invalid_argument("missing nonnegative power");
            }
            const Grid matrix = read_grid(std::cin, size);
            print_grid(independently_power(matrix, exponent));
        } else if (operation == "diagonal") {
            print_cost(minimum_diagonal(read_grid(std::cin, size)));
            std::cout << '\n';
        } else {
            throw std::invalid_argument("unknown independent min-plus operation");
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
    return 0;
}
