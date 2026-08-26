#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

struct NodeRecord {
    int chosen;
    int waiting;
};

struct ArcRecord {
    int tail;
    int head;
    int cost;
};

int row_bits(int width) {
    if (width != 5 && width != 6 && width != 7) {
        throw std::invalid_argument("width must be 5, 6, or 7");
    }
    return (1 << width) - 1;
}

int vertical_cover(int chosen, int width) {
    const int rows = row_bits(width);
    return ((chosen << 1) | (chosen >> 1)) & rows;
}

int pending_after(int left_chosen, int right_chosen, int width) {
    const int rows = row_bits(width);
    return rows & ~(left_chosen | vertical_cover(right_chosen, width));
}

int bit_count(int mask) {
    int total = 0;
    for (int value = mask; value > 0; value >>= 1) {
        total += value & 1;
    }
    return total;
}

std::vector<NodeRecord> build_nodes(int width) {
    const int rows = row_bits(width);
    std::vector<NodeRecord> nodes;
    for (int chosen = 0; chosen <= rows; ++chosen) {
        const int covered_vertically = vertical_cover(chosen, width);
        for (int waiting = 0; waiting <= rows; ++waiting) {
            if ((waiting & covered_vertically) == 0) {
                nodes.push_back({chosen, waiting});
            }
        }
    }
    return nodes;
}

long long key_for(int chosen, int waiting) {
    return (static_cast<long long>(chosen) << 32) | static_cast<unsigned int>(waiting);
}

std::vector<ArcRecord> build_arcs(const std::vector<NodeRecord>& nodes, int width) {
    const int rows = row_bits(width);
    std::unordered_map<long long, int> index_by_pair;
    for (int index = 0; index < static_cast<int>(nodes.size()); ++index) {
        index_by_pair[key_for(nodes[index].chosen, nodes[index].waiting)] = index;
    }

    std::vector<ArcRecord> arcs;
    for (int tail = 0; tail < static_cast<int>(nodes.size()); ++tail) {
        const NodeRecord node = nodes[tail];
        for (int next_chosen = 0; next_chosen <= rows; ++next_chosen) {
            if ((node.waiting & ~next_chosen) != 0) {
                continue;
            }
            const int next_waiting = pending_after(node.chosen, next_chosen, width);
            const auto found = index_by_pair.find(key_for(next_chosen, next_waiting));
            if (found == index_by_pair.end()) {
                throw std::logic_error("missing reconstructed head");
            }
            arcs.push_back({tail, found->second, bit_count(next_chosen)});
        }
    }
    return arcs;
}

std::vector<int> seen_from_zero(const std::vector<std::vector<int>>& graph) {
    std::vector<int> seen(graph.size(), 0);
    std::queue<int> pending;
    seen[0] = 1;
    pending.push(0);
    while (!pending.empty()) {
        const int node = pending.front();
        pending.pop();
        for (int head : graph[node]) {
            if (seen[head] == 0) {
                seen[head] = 1;
                pending.push(head);
            }
        }
    }
    return seen;
}

bool all_seen(const std::vector<int>& seen) {
    return std::find(seen.begin(), seen.end(), 0) == seen.end();
}

bool strongly_connected(int node_count, const std::vector<ArcRecord>& arcs) {
    std::vector<std::vector<int>> forward(node_count);
    std::vector<std::vector<int>> reverse(node_count);
    for (const ArcRecord arc : arcs) {
        forward[arc.tail].push_back(arc.head);
        reverse[arc.head].push_back(arc.tail);
    }
    return all_seen(seen_from_zero(forward)) && all_seen(seen_from_zero(reverse));
}

void write_json(const std::vector<NodeRecord>& nodes, const std::vector<ArcRecord>& arcs) {
    std::cout << "{\"states\":[";
    for (int i = 0; i < static_cast<int>(nodes.size()); ++i) {
        if (i != 0) {
            std::cout << ",";
        }
        std::cout << "[" << nodes[i].chosen << "," << nodes[i].waiting << "]";
    }
    std::cout << "],\"transitions\":[";
    for (int i = 0; i < static_cast<int>(arcs.size()); ++i) {
        if (i != 0) {
            std::cout << ",";
        }
        std::cout << "[" << arcs[i].tail << "," << arcs[i].head << "," << arcs[i].cost << "]";
    }
    std::cout << "],\"strongly_connected\":";
    std::cout << (strongly_connected(static_cast<int>(nodes.size()), arcs) ? "true" : "false");
    std::cout << "}\n";
}

int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "usage: independent_transitions WIDTH\n";
        return 2;
    }
    try {
        const int width = std::stoi(argv[1]);
        const std::vector<NodeRecord> nodes = build_nodes(width);
        const std::vector<ArcRecord> arcs = build_arcs(nodes, width);
        write_json(nodes, arcs);
    } catch (const std::exception& error) {
        std::cerr << error.what() << "\n";
        return 1;
    }
    return 0;
}
