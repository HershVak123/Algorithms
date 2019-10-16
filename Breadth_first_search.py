# -*- coding: utf-8 -*-


class Bfs:

    def __init__(self, graph ):
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
        return explored

    def bfs_shortest(self, start, end):
        """
        This function will calculate the shortest path between the two points on a graph.

        :param start: The starting point on the graph (string)
        :param end: The ending point on the graph (string)
        :return: Returns a list containing the shortest path between the start and end point
        """

        explored = []

        queue = [[start]]

        if start == end:
            return "These two points are adjacent."

        while queue:

            path = queue.pop(0)

            node = path[-1]

            if node not in explored:
                neighbors = self.graph[node]

                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == end:
                        return new_path

                explored.append(node)

        return "These two nodes are not connected."
