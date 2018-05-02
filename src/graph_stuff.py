
def construct_graph(part1):
    g = graph()
    last_char = None
    for c in part1:
        in_list = False
        for n in g.nodes:
            if n.char == c:
                in_list = True
            if n.char == last_char:
                n.edges.add(c)
        if not in_list:
            n = node(c)
            n.edges.add(last_char)
            g.nodes.add(n)

        last_char = c

    return g




def delete_nodes(g, val1):
    gn = set(g.nodes)
    for n in gn:
        ne = set(n.edges)
        if n.char == val1:
            g.nodes.discard(n)

    return g


def find_disconnected_nodes(g):
    dc_nodes = []
    for n in g.nodes:
        if n.edges != set():
            dc_nodes.append(n.char)
    return dc_nodes
class node:
    char = None

    def __init__(self, char):
        self.char = char
        self.edges = set()

class graph:
    def __init__(self):
        self.nodes = set()
