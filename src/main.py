import sys

from src.string_stuff import frequent_character, split_string
from src.tree_stuff import construct_tree, hash_tree

from src.graph_stuff import construct_graph, delete_nodes, \
    find_disconnected_nodes


def main():
    arg = sys.argv[1]
    h = execute(arg)
    print(h)
    return h


if __name__ == "__main__":
    main()


def execute(arg):
    val1 = frequent_character(arg)

    part1, part2 = split_string(arg)

    g = construct_graph(part1)

    g = delete_nodes(g, val1)

    nodes = find_disconnected_nodes(g)

    t = construct_tree(part2)

    h = hash_tree(t, nodes)

    return h