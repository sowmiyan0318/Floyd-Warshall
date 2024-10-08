def floyd_warshall(graph):
    # Create a distance matrix to store the shortest distance between all pairs of vertices
    distance = [[float('inf')] * len(graph) for _ in range(len(graph))]

    # Initialize the distance matrix with the weights of the edges in the graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]

    # Iterate over all vertices in the graph, and for each vertex, iterate over all pairs of vertices
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # For each pair of vertices, check if the path through the current vertex is shorter than the current shortest path
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance

# Example usage:
graph = [
    [0, 3, 8, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 4],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0]
]
distance = floyd_warshall(graph)
print("Shortest distances between all pairs of vertices:")
for row in distance:
    print(row)
