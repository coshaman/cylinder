#include <algorithm>
#include <stdexcept>
#include <vector>

namespace automaton {

struct State {
    int selected;
    int pending;
};

int all_rows(int width) {
    if (width < 5 || width > 7) {
        throw std::invalid_argument("width must be 5, 6, or 7");
    }
    return (1 << width) - 1;
}

int open_vertical(int selected, int width) {
    return ((selected << 1) | (selected >> 1)) & all_rows(width);
}

int next_pending(int previous, int current, int width) {
    return all_rows(width) & ~(previous | open_vertical(current, width));
}

std::vector<State> generate_states(int width) {
    const int limit = 1 << width;
    const int rows = all_rows(width);
    std::vector<State> states;

    for (int selected = 0; selected < limit; ++selected) {
        const int allowed_pending = rows & ~open_vertical(selected, width);
        for (int pending = allowed_pending;; pending = (pending - 1) & allowed_pending) {
            states.push_back({selected, pending});
            if (pending == 0) {
                break;
            }
        }
    }

    std::sort(states.begin(), states.end(), [](const State& a, const State& b) {
        if (a.selected != b.selected) {
            return a.selected < b.selected;
        }
        return a.pending < b.pending;
    });
    return states;
}

}  // namespace automaton
