#BFS searches in level/ layers of neighbors starting from a node
# o(V+E) verticies and edges
# has queue of nodes to visit next
# start @ 0 enqueue neighbors, then enqueue the neighbors neighbors, dont enqueue duplicates
# as neighbors are visited the starting node is dequeue as its neighbors are visited and enqueued
#  