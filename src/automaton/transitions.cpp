#include <algorithm>
#include <map>
#include <stdexcept>
#include <utility>
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

int next_pending(int previous, int current, int width);
std::vector<State> generate_states(int width);

int popcount(int mask) {
    int count = 0;
    while (mask != 0) {
        count += mask & 1;
        mask >>= 1;
    }
    return count;
}

std::vector<Edge> generate_transitions(int width) {
    const std::vector<State> states = generate_states(width);
    std::map<std::pair<int, int>, int> state_index;
    for (int index = 0; index < static_cast<int>(states.size()); ++index) {
        state_index[{states[index].selected, states[index].pending}] = index;
    }

    const int limit = 1 << width;
    std::vector<Edge> edges;
    for (int tail = 0; tail < static_cast<int>(states.size()); ++tail) {
        const State& state = states[tail];
        for (int next_selected = 0; next_selected < limit; ++next_selected) {
            if ((state.pending & ~next_selected) != 0) {
                continue;
            }
            const int pending = next_pending(state.selected, next_selected, width);
            const auto found = state_index.find({next_selected, pending});
            if (found == state_index.end()) {
                throw std::logic_error("generated transition head is not a state");
            }
            edges.push_back({tail, found->second, popcount(next_selected)});
        }
    }

    std::sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) {
        if (a.tail != b.tail) {
            return a.tail < b.tail;
        }
        if (a.head != b.head) {
            return a.head < b.head;
        }
        return a.weight < b.weight;
    });
    return edges;
}

}  // namespace automaton
