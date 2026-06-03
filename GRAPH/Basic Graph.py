from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self):
        v = input("Enter vertex: ")
        if v not in self.graph:
            self.graph[v] = []
            print("Vertex added Successfully")
        else:
            print("Vertex already exists")

    def add_edge(self):
        u = input("Enter Start vertex: ")
        v = input("Enter End vertex: ")
        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u) # UNDIRECTED GRAP HAI ISILIYE DONO POINTS K LIYE LIKHA HAI
            print("Edge added Successfully")
        else:
            print("Invalid Vertex")

    def display(self):
        print("graph Adjacency list: ")
        for vertex in self.graph:
            print(vertex," -> ",self.graph[vertex])

    def bfs_traversal(self):
        start = input("Enter start vertex: ")
        if start not in self.graph:
            print("Vertex does not exist")
            return

        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end = " ")
                visited.add(node)
            for neighbors in self.graph[node]:
                if neighbors not in visited:
                    queue.append(neighbors)
        print()

    def dfs_traversal(self):
        start = input("Enter start vertex: ")
        if start not in self.graph:
            print("Vertex does not exist")
            return

        visited = set()
        print("DFS traversal")
        self.dfs_util(start,visited) #recurssion function
        print()

    def dfs_util(self,start,visited):
        visited.add(start)
        print(start,end = " ")
        for neighbors in self.graph[start]:
            if neighbors not in visited:
                self.dfs_util(neighbors,visited)
g = Graph()

while True:
    print("\n--- Graph Menu ---")
    print("1. Add Vertex")
    print("2. Add Edge")
    print("3. Display Graph")
    print("4. BFS Traversal")
    print("5. DFS Traversal")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        g.add_vertex()
    elif choice == 2:
        g.add_edge()
    elif choice == 3:
        g.display()
    elif choice == 4:
        g.bfs_traversal()
    elif choice == 5:
        g.dfs_traversal()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
