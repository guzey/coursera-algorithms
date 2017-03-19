import networkx as nx
import random
import math


def contraction(graph):
    g = graph
    for i in range(0, g.number_of_nodes() - 2):
        nodes_to_contract = random.choice(g.edges())
        node_to_stay = nodes_to_contract[0]
        node_to_remove = nodes_to_contract[1]
        for edge in [node[1] for node in g.edges(node_to_remove)]:
            g.add_edge(node_to_stay, edge)
        g.remove_node(node_to_remove)
        for edge in g.selfloop_edges():
            g.remove_edge(edge[0], edge[0])


def main():
    min_cut = 1000000000
    g = nx.MultiGraph(data=nx.read_adjlist("_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt", nodetype=int))
    # the chosen number of iteration ensures almost certain success of the algorithm
    for i in range(0, math.ceil(g.number_of_nodes() * math.log(g.number_of_nodes()))):
        g = nx.MultiGraph(data=nx.read_adjlist("_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt", nodetype=int))
        contraction(g)
        if g.number_of_edges() < min_cut:
            min_cut = g.number_of_edges()
        print(min_cut)


if __name__ == "__main__":
    main()
