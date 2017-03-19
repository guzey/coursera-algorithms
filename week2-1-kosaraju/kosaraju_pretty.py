import time

# each node is assigned its leader, its finishing time and its neighboring edges
class Node():
    def __init__(self):
        self.leader = ""
        self.finishing_time = ""
        self.explored_indicator = False
        self.neighbors = []


def dfsl(graph, processing_order):

    # reset the explored indicator before running the discovery process
    for node in graph:
        node.explored_indicator = False

    '''
    not recursive, since I figured that for a large graph this implementation with a stack is preferable;
    used a nested function because of variable scope, e.g. 'leader' variable would have to be global otherwise
    '''
    def dfs(graph, node):
        nonlocal finishing_time
        graph_to_explore = [node]

        graph[node].explored_indicator = True

        graph[node].leader = leader
        edges_to_explore = graph

        # here we iterate on the stack of unexplored nodes of a graph
        while graph_to_explore:
            last_node = graph_to_explore[-1]

            # an indicator for whether we have explored all the neighbors of the node
            all_neighbors_explored = True

            # iterate over these neighbors
            for out_node in edges_to_explore[last_node].neighbors:

                # if the node is not explored
                if not graph[out_node].explored_indicator:

                    all_neighbors_explored = False

                    # then we note it as explored
                    graph[out_node].explored_indicator = True

                    # and put it on top of the stack
                    graph_to_explore.append(out_node)

                    '''
                    the line below is a slight optimization that makes us skip the edges we have already looked at
                    in the past iterations; strictly speaking this makes the parent for loop wrong, since it counts
                    the number of out_node's wrongly, upon the removal of them in the process, but it's okay here,
                    since the preceding not_explored_neighbors_of_a_node == 0 will never satisfy in that case!
                    '''
                    edges_to_explore[last_node].neighbors.remove(out_node)

            '''
            if we have explored all the neighbors of a node (or if it has no neigbors,
            then assign leader to it and set its finishing time
            '''
            if all_neighbors_explored == True:
                graph[graph_to_explore[-1]].leader = node
                graph[graph_to_explore.pop()].finishing_time = finishing_time
                finishing_time += 1

    # reset finishing time before running the loop
    finishing_time = 0

    # note that the processing_order is always reverse (put it in the function call for better intuition)
    for node in processing_order:

        # if the node is unexplored, then explore it with a dfs and set it as the leader for all the reachable nodes
        if not graph[node].explored_indicator:
            # note that we only need leaders for the second run of the loop when we count sccs
            leader = node
            dfs(graph, node)


def main():
    start_time = time.time()
    time.clock()

    graph_txt = '2.txt'
    # graph_txt = 'scc.txt'

    # assuming that the edge list is sorted, this gets its number of nodes
    num_lines = sum(1 for line in open(graph_txt))
    with open(graph_txt) as file:
        num_nodes = int((file.readlines()[num_lines - 1]).split()[0])

    graph = [Node() for x in range(0, num_nodes)]
    reversed_graph = [Node() for x in range(0, num_nodes)]

    # creates edge lists from a given txt
    with open(graph_txt) as file:
        for line in file:
            u, v = line.split()
            u = int(u)
            v = int(v)
            graph[u - 1].neighbors.append(v - 1)
            reversed_graph[v - 1].neighbors.append(u - 1)
        print("edge list done!")

    dfsl_time_start = time.time()
    dfsl(reversed_graph, reversed(range(0,num_nodes)))
    dfsl_time = time.time() - dfsl_time_start

    # creates a dictionary with each node paired with its finishing time
    nodes_finishing_time = dict(zip(range(0,num_nodes), [node.finishing_time for node in reversed_graph]))

    # creates a list with nodes ordered by their finishing time
    nodes_ordered_by_finishing_time = [edge[0] for edge in sorted(nodes_finishing_time.items(), key=lambda x: x[1])]

    dfsl(graph, reversed(nodes_ordered_by_finishing_time))

    # creates a dictionary with each node paired with the number of nodes it was leader for during the second dfsl
    leaders = {}
    for node in range(0,num_nodes):
        if graph[node].leader in leaders:
            leaders[graph[node].leader] += 1
        else:
            leaders[graph[node].leader] = 1

    print("[up to] five largest sccs:", sorted(leaders.values(), reverse=True)[:5])

    end_time = time.time() - start_time
    print("dfsl time:", dfsl_time)
    print("whole program time:", end_time)

if __name__ == "__main__":
    main()