# A dfs-based algorithm that finds the largest connected components of a graph, and prints out the largest 5 of them

import time

start = time.time()
time.clock()

graph = '2.txt'
# graph = 'scc.txt'

# assuming that the edge list is sorted, this gets its number of nodes
num_lines = sum(1 for line in open(graph))
with open(graph) as file:
    num_nodes = int((file.readlines()[num_lines-1]).split()[0])

edge_list = [[] for x in range(0,num_nodes)]
reversed_edge_list = [[] for x in range(0,num_nodes)]

with open(graph) as file:
    for line in file:
        u, v = line.split()
        u = int(u)
        v = int(v)
        # adj_matrix[u-1, v-1] = 1
        edge_list[u-1].append(v-1)
        reversed_edge_list[v-1].append(u-1)
    print("edge list done!")

# each node is assigned a number, its leader, its finishing time and its neighboring edges
class Node():
    def __init__(self):
        self.number = ""
        self.leader = ""
        self.finishing_time = ""
        # self.out_edges = []
        self.not_explored_edges = []
        self.explored_indicator = False


graph_nodes_numbers = [x for x in range(0,num_nodes)]
graph_nodes = [x for x in range(0,num_nodes)]

# these vars are global since used both in dfs loop and in dfs
graph_explored = []
finishing_time = 0
leader = 0
edges_to_explore = []

# not recursive since it had stack overflow problems
def dfs(g, node):
    global finishing_time, graph_explored, edges_to_explore, graph_nodes
    graph_to_explore = [node]
    graph_explored.append(node)
    graph_nodes[node].explored_indicator = True
    graph_nodes[node].leader = leader
    edges_to_explore = g
    while graph_to_explore:
        last_node = graph_to_explore[-1]
        not_explored_edges_of_a_node = 0
        if edges_to_explore[last_node]:
            for out_node in edges_to_explore[last_node]:
                # print(edges_to_explore[last_node])
                if not graph_nodes[out_node].explored_indicator and not_explored_edges_of_a_node == 0:
                    graph_explored.append(out_node)
                    graph_nodes[out_node].explored_indicator = True
                    graph_to_explore.append(out_node)
                    not_explored_edges_of_a_node += 1
                    edges_to_explore[last_node].remove(out_node)
            if not_explored_edges_of_a_node == 0:
                #  and graph_nodes[graph_to_explore[-1]].leader == ""
                graph_nodes[graph_to_explore[-1]].leader = node
                graph_nodes[graph_to_explore.pop()].finishing_time = finishing_time
                finishing_time += 1
            # elif not_explored_edges_of_a_node == 0 and graph_nodes[graph_to_explore[-1]].leader != "":
                # graph_to_explore.pop()
        elif graph_nodes[graph_to_explore[-1]].leader != graph_to_explore[-1]:
            graph_nodes[graph_to_explore[-1]].leader = node
            graph_nodes[graph_to_explore.pop()].finishing_time = finishing_time
            finishing_time += 1
        else:
            graph_explored.append(node)
            graph_nodes[node].explored_indicator = True
            graph_nodes[graph_to_explore[-1]].leader = node
            graph_nodes[graph_to_explore.pop()].finishing_time = finishing_time
            finishing_time += 1

def dfsl(g, ordered_nodes):
    global finishing_time, leader, graph_explored, graph_nodes
    graph_explored = []
    for x in graph_nodes:
        x.explored_indicator = False
    edges_to_explore = []
    finishing_time = 0
    count = 0
    new_time = time.clock()
    for node in reversed(ordered_nodes):
        if not graph_nodes[node].explored_indicator:
            count += 1
            if count % 1000 == 0:
                print(count)
                time_diff = time.clock() - new_time
                new_time = time.clock()
                print(time_diff)
            leader = node
            dfs(g, node)

for x in graph_nodes:
    graph_nodes[x] = Node()
    graph_nodes[x].number = x

dfsl_time_start = time.time()
dfsl(reversed_edge_list, graph_nodes_numbers)
dfsl_time = time.time() - dfsl_time_start
di = dict(zip(graph_nodes_numbers,[node.finishing_time for node in graph_nodes]))

nodes_ordered_by_finishing_time = [edge[0] for edge in sorted(di.items(), key=lambda x:x[1])]

dfsl(edge_list, nodes_ordered_by_finishing_time)

leaders = {}
for node in graph_nodes_numbers:
    if graph_nodes[node].leader in leaders:
        leaders[graph_nodes[node].leader] += 1
    else:
        leaders[graph_nodes[node].leader] = 1

print(sorted(leaders.values(), reverse=True)[:5])
end = time.time() - start
print(end)
print(dfsl_time)