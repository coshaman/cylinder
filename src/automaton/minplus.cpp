#include <algorithm>
#include <cstddef>
#include <cstdint>
#include <iostream>
#include <limits>
#include <optional>
#include <sstream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

namespace automaton {

class Integer {
public:
    explicit Integer(long long value = 0)
        : Integer(std::to_string(value)) {}

    explicit Integer(const std::string& text) {
        if (text.empty()) {
            throw std::invalid_argument("empty integer");
        }
        std::size_t first_digit = 0;
        if (text[0] == '-' || text[0] == '+') {
            negative_ = text[0] == '-';
            first_digit = 1;
        }
        if (first_digit == text.size()) {
            throw std::invalid_argument("invalid integer");
        }
        for (std::size_t index = first_digit; index < text.size(); ++index) {
            if (text[index] < '0' || text[index] > '9') {
                throw std::invalid_argument("invalid integer");
            }
        }
        digits_ = text.substr(first_digit);
        normalize();
    }

    friend Integer operator+(const Integer& left, const Integer& right) {
        if (left.negative_ == right.negative_) {
            return from_parts(left.negative_, add_abs(left.digits_, right.digits_));
        }
        const int order = compare_abs(left.digits_, right.digits_);
        if (order == 0) {
            return Integer(0);
        }
        if (order > 0) {
            return from_parts(left.negative_, subtract_abs(left.digits_, right.digits_));
        }
        return from_parts(right.negative_, subtract_abs(right.digits_, left.digits_));
    }

    friend bool operator<(const Integer& left, const Integer& right) {
        if (left.negative_ != right.negative_) {
            return left.negative_;
        }
        const int order = compare_abs(left.digits_, right.digits_);
        return left.negative_ ? order > 0 : order < 0;
    }

    friend std::ostream& operator<<(std::ostream& output, const Integer& value) {
        if (value.negative_ && value.digits_ != "0") {
            output << '-';
        }
        output << value.digits_;
        return output;
    }

private:
    bool negative_ = false;
    std::string digits_ = "0";

    static int compare_abs(const std::string& left, const std::string& right) {
        if (left.size() != right.size()) {
            return left.size() < right.size() ? -1 : 1;
        }
        if (left == right) {
            return 0;
        }
        return left < right ? -1 : 1;
    }

    static std::string add_abs(const std::string& left, const std::string& right) {
        std::string result;
        int carry = 0;
        std::size_t i = left.size();
        std::size_t j = right.size();
        while (i > 0 || j > 0 || carry != 0) {
            const int first = i > 0 ? left[--i] - '0' : 0;
            const int second = j > 0 ? right[--j] - '0' : 0;
            const int total = first + second + carry;
            result.push_back(static_cast<char>('0' + total % 10));
            carry = total / 10;
        }
        std::reverse(result.begin(), result.end());
        return result;
    }

    static std::string subtract_abs(const std::string& larger, const std::string& smaller) {
        std::string result;
        int borrow = 0;
        std::size_t i = larger.size();
        std::size_t j = smaller.size();
        while (i > 0) {
            int difference = (larger[--i] - '0') - borrow;
            if (j > 0) {
                difference -= smaller[--j] - '0';
            }
            if (difference < 0) {
                difference += 10;
                borrow = 1;
            } else {
                borrow = 0;
            }
            result.push_back(static_cast<char>('0' + difference));
        }
        std::reverse(result.begin(), result.end());
        const std::size_t first = result.find_first_not_of('0');
        return first == std::string::npos ? "0" : result.substr(first);
    }

    static Integer from_parts(bool negative, std::string digits) {
        Integer result;
        result.negative_ = negative;
        result.digits_ = std::move(digits);
        result.normalize();
        return result;
    }

    void normalize() {
        const std::size_t first = digits_.find_first_not_of('0');
        digits_ = first == std::string::npos ? "0" : digits_.substr(first);
        if (digits_ == "0") {
            negative_ = false;
        }
    }
};

using Entry = std::optional<Integer>;

struct Matrix {
    std::size_t rows;
    std::size_t cols;
    std::vector<Entry> values;

    Matrix(std::size_t row_count, std::size_t column_count)
        : rows(row_count), cols(column_count), values(checked_size(row_count, column_count)) {}

    static std::size_t checked_size(std::size_t row_count, std::size_t column_count) {
        if (column_count != 0 && row_count > std::numeric_limits<std::size_t>::max() / column_count) {
            throw std::length_error("matrix dimensions overflow");
        }
        return row_count * column_count;
    }

    Entry& at(std::size_t row, std::size_t column) {
        return values[row * cols + column];
    }

    const Entry& at(std::size_t row, std::size_t column) const {
        return values[row * cols + column];
    }
};

Entry minplus_add(const Entry& left, const Entry& right) {
    if (!left || !right) {
        return std::nullopt;
    }
    return *left + *right;
}

Matrix minplus_multiply(const Matrix& left, const Matrix& right) {
    if (left.cols != right.rows) {
        throw std::invalid_argument("min-plus dimension mismatch");
    }

    Matrix product(left.rows, right.cols);
    for (std::size_t row = 0; row < left.rows; ++row) {
        for (std::size_t column = 0; column < right.cols; ++column) {
            Entry best = std::nullopt;
            for (std::size_t middle = 0; middle < left.cols; ++middle) {
                const Entry candidate = minplus_add(left.at(row, middle), right.at(middle, column));
                if (candidate && (!best || *candidate < *best)) {
                    best = candidate;
                }
            }
            product.at(row, column) = best;
        }
    }
    return product;
}

Matrix minplus_identity(std::size_t size) {
    Matrix identity(size, size);
    for (std::size_t index = 0; index < size; ++index) {
        identity.at(index, index) = Integer(0);
    }
    return identity;
}

Matrix minplus_power(const Matrix& base, std::uint64_t exponent) {
    if (base.rows != base.cols) {
        throw std::invalid_argument("min-plus power requires a square matrix");
    }

    Matrix result = minplus_identity(base.rows);
    Matrix factor = base;
    while (exponent != 0) {
        if ((exponent & 1U) != 0) {
            result = minplus_multiply(result, factor);
        }
        exponent >>= 1U;
        if (exponent != 0) {
            factor = minplus_multiply(factor, factor);
        }
    }
    return result;
}

Entry diagonal_minimum(const Matrix& matrix) {
    Entry best = std::nullopt;
    const std::size_t diagonal_size = matrix.rows < matrix.cols ? matrix.rows : matrix.cols;
    for (std::size_t index = 0; index < diagonal_size; ++index) {
        const Entry& candidate = matrix.at(index, index);
        if (candidate && (!best || *candidate < *best)) {
            best = candidate;
        }
    }
    return best;
}

namespace {

Entry parse_entry(const std::string& token) {
    if (token == "INF") {
        return std::nullopt;
    }
    return Integer(token);
}

std::size_t read_size(std::istream& input) {
    std::size_t size = 0;
    if (!(input >> size)) {
        throw std::invalid_argument("missing matrix size");
    }
    return size;
}

Matrix read_matrix(std::istream& input, std::size_t rows, std::size_t cols) {
    Matrix matrix(rows, cols);
    std::string token;
    for (std::size_t index = 0; index < matrix.values.size(); ++index) {
        if (!(input >> token)) {
            throw std::invalid_argument("missing matrix entry");
        }
        matrix.values[index] = parse_entry(token);
    }
    return matrix;
}

void write_entry(const Entry& entry) {
    if (entry) {
        std::cout << *entry;
    } else {
        std::cout << "INF";
    }
}

void write_matrix(const Matrix& matrix) {
    std::cout << matrix.rows << ' ' << matrix.cols;
    for (const Entry& entry : matrix.values) {
        std::cout << ' ';
        write_entry(entry);
    }
    std::cout << '\n';
}

}  // namespace

}  // namespace automaton

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: minplus {multiply|power|diagonal}\n";
        return 2;
    }

    try {
        const std::string operation = argv[1];
        if (operation == "multiply") {
            const std::size_t size = automaton::read_size(std::cin);
            const automaton::Matrix left = automaton::read_matrix(std::cin, size, size);
            const automaton::Matrix right = automaton::read_matrix(std::cin, size, size);
            automaton::write_matrix(automaton::minplus_multiply(left, right));
        } else if (operation == "power") {
            const std::size_t size = automaton::read_size(std::cin);
            std::uint64_t exponent = 0;
            if (!(std::cin >> exponent)) {
                throw std::invalid_argument("missing nonnegative power");
            }
            const automaton::Matrix matrix = automaton::read_matrix(std::cin, size, size);
            automaton::write_matrix(automaton::minplus_power(matrix, exponent));
        } else if (operation == "diagonal") {
            const std::size_t size = automaton::read_size(std::cin);
            const automaton::Matrix matrix = automaton::read_matrix(std::cin, size, size);
            automaton::write_entry(automaton::diagonal_minimum(matrix));
            std::cout << '\n';
        } else {
            throw std::invalid_argument("unknown min-plus operation");
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
    return 0;
}
