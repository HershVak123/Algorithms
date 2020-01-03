# -*- coding: utf-8 -*-
import sys


class DijkstrasGraph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        self.description = "Dijkstra's algorithm will calculate the shortest distance between " \
                           "two nodes given that edges between two nodes have a cost associated " \
                           "with them."

    def print_soln(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", "\t", dist[node])

    def min_distance(self, dist, sptSet):

        min_dist = sys.maxsize

        for v in range(self.V):
            if dist[v] < min_dist and sptSet[v] is False:
                min_dist = dist[v]

                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for count in range(self.V):

            u = self.min_distance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] is False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_soln(dist)


g = DijkstrasGraph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

g.dijkstra(7)