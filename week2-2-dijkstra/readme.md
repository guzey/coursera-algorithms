This week we weare asked to implement the Dijkstra's algorithms for finding shortest paths between nodes of a graph. Here is a naive implementation of this algorithm, without the use of heaps.

The explanation of the algorithm is here: https://www.coursera.org/learn/algorithms-graphs-data-structures/lecture/Pbpp9/dijkstras-algorithm-implementation-and-running-time

The heap version of the algorithm would only update distances for newly explored edges. Default heapq library implements heaps as lists, which means that constant time lookup of the nodes, associated with distances from the source node is not possible with it. Instead, the heap would need to be implemented as a dictionary, to allow for fast lookup of nodes.

dijkstra_naive.py is the algorithm.

1.txt is a test graph from Coursera forums