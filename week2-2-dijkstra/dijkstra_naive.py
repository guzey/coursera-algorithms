'''
this is a naive implementation of the dijkstra algorithm, without the use of heaps
'''

import time
from operator import itemgetter


# this function computes the shortest path from the source node to all other nodes of an undirected graph
def dijkstra(graph, source_node):
    global num_nodes

    # a dictionary to store shortest paths to all nodes
    shortest_paths = {source_node: 0}

    # explore the graph until all shortest paths are calculated
    while len(shortest_paths) < num_nodes:

        # a dictionary to store potential nodes to explore in the current iteration
        shortest_paths_candidates = {}

        # now we need to iterate over all edges going from the explored nodes to unexplored edges

        # so for each node in the explored set
        for node in shortest_paths:

            # and for every edge of this node
            for out_node in graph[node]:

                # if the edge leads to a new node
                if out_node not in shortest_paths:

                    # then it could potentially be a shortest path to the new node, so we calculate greedy score
                    path_length = shortest_paths[node] + graph[node][out_node]

                    # if this edge is the first one leading to a new node, then we record the path as a candidate
                    if out_node not in shortest_paths_candidates:
                        shortest_paths_candidates[out_node] = shortest_paths[node] + graph[node][out_node]

                    # if this edge is not the first one, then we record it only if it's better than the previous
                    elif path_length < shortest_paths_candidates[out_node]:
                        shortest_paths_candidates[out_node] = path_length

        # check which one of all potential nodes is closest to the source node
        node_to_add = min(shortest_paths_candidates, key=shortest_paths_candidates.get)

        # add the closet node to the explored set and set its distance from the source node
        shortest_paths[node_to_add] = shortest_paths_candidates[node_to_add]

    return shortest_paths


def main():
    global num_nodes
    start_time = time.time()
    time.clock()

    graph_txt = '1.txt'

    # assuming that there's one node per line this will get the number of nodes in a graph
    num_nodes = sum(1 for line in open(graph_txt))

    graph = [None] * num_nodes

    # creates edge lists from a given txt
    with open(graph_txt) as file:
        current_node = 0
        for line in file:

            '''
            store graph as a list of dictionaries. Every dictionary corresponds to one node and every item in a
            dictionary corresponds to one edge. Keys are connected nodes, values are distances to respective nodes
            '''
            graph[current_node] = {}

            for edge in line.split()[1:]:
                node, length = edge.split(',')
                node = int(node)
                length = int(length)

                graph[current_node][node - 1] = length

            current_node += 1

    # prints out distances to selected nodes
    print(itemgetter(1, 4, 6)(dijkstra(graph, 0)))
    end_time = time.time() - start_time
    print("time to run:", end_time)


if __name__ == "__main__":
    main()
