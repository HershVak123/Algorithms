import sys

inf = sys.maxsize


class FWGraph:

    def __init__(self, weights):
        self.weights = weights
        self.V = len(weights)

    def floyd_warshall(self):
        distance_matrix = self.weights
        for k in range(self.V):
            next_distance_matrix = [list(row) for row in distance_matrix]  # make a copy of distance matrix
            for i in range(self.V):
                for j in range(self.V):
                    # Choose if the k vertex can work as a path with shorter distance
                    next_distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
            distance_matrix = next_distance_matrix  # update
        return distance_matrix


# A graph represented as Adjacency matrix
graph = [
    [0, inf, inf, -3],
    [inf, 0, inf, 8],
    [inf, 4, 0, -2],
    [5, inf, 3, 0]]

FW = FWGraph(graph)

print(FW.floyd_warshall())
