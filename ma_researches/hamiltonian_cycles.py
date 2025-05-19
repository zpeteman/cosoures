class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, pos, path):
        # Check if this vertex is an adjacent vertex of the previously added vertex
        if self.graph[path[pos-1]][v] == 0:
            return False

        # Check if this vertex has already been included in the path
        if v in path:
            return False

        return True

    def hamiltonian_cycle_util(self, path, pos):
        # Base case: if all vertices are included in the path
        if pos == self.V:
            # Last vertex must be adjacent to the first vertex in path
            # to make a cycle
            if self.graph[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False

        # Try different vertices as next candidate in the Hamiltonian Cycle
        for v in range(1, self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                
                if self.hamiltonian_cycle_util(path, pos + 1):
                    return True

                # Remove current vertex if it doesn't lead to a solution
                path[pos] = -1

        return False

    def hamiltonian_cycle(self):
        path = [-1] * self.V
        path[0] = 0  # Start from vertex 0

        if not self.hamiltonian_cycle_util(path, 1):
            print("Solution does not exist")
            return False

        self.print_solution(path)
        return True

    def print_solution(self, path):
        print("Solution Exists: Following is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    g1 = Graph(5)
    g1.graph = [[0, 1, 0, 1, 0],
               [1, 0, 1, 1, 1],
               [0, 1, 0, 0, 1],
               [1, 1, 0, 0, 1],
               [0, 1, 1, 1, 0]]
    
    print("Graph 1:")
    g1.hamiltonian_cycle()
    
    # Create another sample graph
    g2 = Graph(5)
    g2.graph = [[0, 1, 0, 1, 0],
               [1, 0, 1, 1, 1],
               [0, 1, 0, 0, 1],
               [1, 1, 0, 0, 0],
               [0, 1, 1, 0, 0]]
    
    print("\nGraph 2:")
    g2.hamiltonian_cycle()
