import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        minimum = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if key[v] < minimum and not mst_set[v]:
                minimum = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        mst_set = [False] * self.V

        key[0] = 0

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not mst_set[v]
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        # Print MST and calculate total cost
        total_cost = 0

        print("\nEdges in Minimum Spanning Tree:")
        print("Edge \tWeight")

        for i in range(1, self.V):
            weight = self.graph[i][parent[i]]
            total_cost += weight
            print(f"{parent[i]} - {i}\t{weight}")

        print("\nMinimum Spanning Tree Cost =", total_cost)


# User Input
vertices = int(input("Enter number of vertices: "))

g = Graph(vertices)

print("Enter adjacency matrix:")

for i in range(vertices):
    row = list(map(int, input().split()))
    for j in range(vertices):
        g.graph[i][j] = row[j]

# Run Prim's Algorithm
g.prim_mst()