# -*- coding: utf-8 -*-


relation_graph = {'A': ['B', 'C', 'E'],
                  'B': ['A', 'D', 'E'],
                  'C': ['A', 'F', 'G'],
                  'D': ['B'],
                  'E': ['A', 'B', 'D'],
                  'F': ['C'],
                  'G': ['C']}


class Bfs:

    def __init__(self, graph):
        self.graph = graph
        self.shortest_path = None
        self.connected_nodes = None

    def bfs_connected(self, start):
        """
        This function is a breadth-first search which takes a starting point (string)
        and returns a list of all explorable nodes from that point. Can be used to
        check if two points are connected on a graph. Graph relations are defined as
        a dictionary of adjacency lists.

        :param start: Starting point for search (string)
        :return: Returns a list of all explorable nodes from the starting point
        """

        # Initialize the explored list.
        explored = []

        # Initialize the queue with our starting point
        queue = [start]

        while queue:

            # De-queue the first value to represent that we visited the node.
            node = queue.pop(0)

            # Add the node to the explored list if it's not already there, then add its neighbors to the queue.
            if node not in explored:
                explored.append(node)

                # call self.graph since it is not an input to the function, but a property of class when instantiated.
                neighbors = self.graph[node]

                for neighbor in neighbors:
                    queue.append(neighbor)

        # Return the list when the queue is finally empty
        self.connected_nodes = explored
        return explored

    def bfs_shortest(self, start, end):
        """
        This function will calculate the shortest path between the two points on a graph.

        :param start: The starting point on the graph (string)
        :param end: The ending point on the graph (string)
        :return: Returns a list containing the shortest path between the start and end point
        """

        # Initialize our explored list
        explored = []

        # Initialize our queue (since our queue will contain paths, each element of the list will be
        # a list in itself
        queue = [[start]]

        # Start with the simplest case
        if start == end:
            return "These two points are adjacent."

        # Iterate over the queue until its empty
        while queue:

            # Take the first list out of the queue
            path = queue.pop(0)

            # Take the last element of the list
            node = path[-1]

            # If that element isn't in explored, add look at the neighbors of the node
            if node not in explored:
                neighbors = self.graph[node]

                # Iterate over each neighbor and and append the node to the path list
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    # If the neighboring node is the end node, then we have found the shortest path
                    if neighbor == end:
                        self.shortest_path = new_path
                        return new_path

                # If none of the neighboring nodes are the end node, append the current node in queue to explored list
                # and begin next iteration
                explored.append(node)

        # If the queue empties and we do not have a shortest path to return, then the two nodes must not be connected
        return "These two nodes are not connected."


if __name__ == '__main__':
    bfs = Bfs(relation_graph)
    print(bfs.bfs_connected('B'))
    print(bfs.bfs_shortest('A', 'G'))

