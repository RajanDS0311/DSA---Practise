import heapq

# Function to find shortest path and actual route
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # To store shortest path
    previous = {node: None for node in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Visit neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update shorter distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous


# Function to print shortest path
def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return []


# ---------------- USER INPUT ----------------

graph = {}

# Number of nodes
n = int(input("Enter number of nodes: "))

# Create graph
for i in range(n):
    node = input(f"\nEnter node {i+1} name: ")
    graph[node] = {}

    edges = int(input(f"How many neighbors for {node}? "))

    for j in range(edges):
        neighbor = input("Enter neighbor node: ")
        weight = int(input("Enter distance/weight: "))

        graph[node][neighbor] = weight

# Starting node
start_node = input("\nEnter starting node: ")

# Ending node
end_node = input("Enter destination node: ")

# Run Dijkstra Algorithm
distances, previous = dijkstra(graph, start_node)

# Get shortest path
path = get_path(previous, start_node, end_node)

# Display result
print("\nShortest distance:", distances[end_node])

print("Shortest path: ", " -> ".join(path))

