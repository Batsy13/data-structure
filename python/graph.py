from abc import ABC, abstractmethod
from collections import defaultdict

class Graph(ABC):
    
    @abstractmethod
    def num_of_vertices(self):
        pass
    
    @abstractmethod
    def num_of_edges(self):
        pass
    
    @abstractmethod
    def degree_sequence(self):
        pass
    
    @abstractmethod
    def add_edge(self, u, v):
        pass
    
    @abstractmethod
    def remove_edge(self, u, v):
        pass
    
    @abstractmethod
    def print_graph(self):
        pass

    @abstractmethod
    def is_simple(self):
        pass

    @abstractmethod
    def is_null(self):
        pass

    @abstractmethod
    def is_complete(self):
        pass

class DenseGraph(Graph):
    
    def __init__(self, num_vertices_or_labels):
        self.vertices_map = {}
        self.indices_map = {}
        self.number_edges = 0
        
        if isinstance(num_vertices_or_labels, int):
            
            self.num_vertices = num_vertices_or_labels
            
            for i in range(self.num_vertices):
                self.vertices_map[i] = i
                self.indices_map[i] = i  
        elif isinstance(num_vertices_or_labels, list):
            
            self.num_vertices = len(num_vertices_or_labels)
            
            for i, label in enumerate(num_vertices_or_labels):
                
                if label in self.vertices_map:
                    raise ValueError(f"Duplicated label '{label}' in the vertex list")
                
                self.vertices_map[label] = i
                self.indices_map[i] = label
            
        else:
            raise ValueError("Argument must be an integer number of vertices or a list of labels")
        
        self.adjacency_matrix = [[0 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        
    def num_of_vertices(self):
        return self.num_vertices
    
    def num_of_edges(self):
        return self.number_edges
    
    def degree_sequence(self):
        degrees = {}
        
        for i in range(self.num_vertices):
            vertex_label = self.indices_map[i]
            degree = 0
            
            for j in range(self.num_vertices):
                if self.adjacency_matrix[i][j] == 1:
                    degree += 1
            
            if self.adjacency_matrix[i][i] == 1:
                degree += 1
            
            degrees[vertex_label] = degree
            
        return list(degrees.values())
    
    def degree_sequence2(self):
        return sorted([sum(row) for row in self.adjacency_matrix])
        
    def _get_index(self, label):
        if label not in self.vertices_map:
            raise ValueError(f"Vertex '{label}' does not exist on graph") 
        
        return self.vertices_map[label]
        
    def add_edge(self, u, v):
        try:
            idx_u = self._get_index(u)
            idx_v = self._get_index(v)
        except:
            print(f"Could not add Edge ({u}, {v})")
            return
        
        if self.adjacency_matrix[idx_u][idx_v] == 0:
            print(f"Vertex added between {u} and {v}")
            self.adjacency_matrix[idx_u][idx_v] = 1
            if u != v:
                self.adjacency_matrix[idx_v][idx_u] = 1
            self.number_edges += 1
              
        
    def remove_edge(self, u, v):
        try:
            idx_u = self._get_index(u)
            idx_v = self._get_index(v)
        except:
            print(f"Could not remove Edge ({u}, {v})")
            
        if self.adjacency_matrix[idx_u][idx_v] == 1:
            print(f"Removing edge between {u} and {v}")
            self.adjacency_matrix[idx_u][idx_v] = 0
            if u != v:
                self.adjacency_matrix[idx_v][idx_u] = 0
            self.number_edges -= 1
        
    def print_graph(self):
        if self.num_of_edges() == 0:
            print("Graph is Empty")
            return
        
        print("\nGraph Representation (Adjacency Matrix):")
        header = "      " + " ".join(f"{self.indices_map[i]:^3}" for i in range(self.num_vertices))
        print(header)
        print("    " + "-" * (len(header) - 3))
        
        for i in range(self.num_vertices):
            vertex_label = self.indices_map[i]
            row_values = " ".join(f"{self.adjacency_matrix[i][j]:^3}" for j in range(self.num_vertices))
            print(f"{vertex_label:^3} | {row_values}")
            
    def is_simple(self):
        for i in range(self.num_vertices):
            if self.adjacency_matrix[i][i] == 1:
                return False
        return True

    def is_null(self):
        return self.number_edges == 0

    def is_complete(self):
        if not self.is_simple():
            return False
        
        expected_edges = self.num_vertices * (self.num_vertices - 1) // 2
        return self.number_edges == expected_edges


class SparseGraph(Graph):
    def __init__(self, num_vertices_or_labels):
        self.vertices_map = {}
        self.indices_map = {}
        self.number_edges = 0
        
        if isinstance(num_vertices_or_labels, int):
            
            self.num_vertices = num_vertices_or_labels
            
            for i in range(self.num_vertices):
                self.vertices_map[i] = i
                self.indices_map[i] = i  
        elif isinstance(num_vertices_or_labels, list):
            
            self.num_vertices = len(num_vertices_or_labels)
            
            for i, label in enumerate(num_vertices_or_labels):
                
                if label in self.vertices_map:
                    raise ValueError(f"Duplicated label '{label}' in the vertex list")
                
                self.vertices_map[label] = i
                self.indices_map[i] = label
            
        else:
            raise ValueError("Argument must be an integer number of vertices or a list of labels")
        
        self.adjacency_list = defaultdict(list) 
        
    def num_of_vertices(self):
        return self.num_vertices
    
    def num_of_edges(self):
        return self.number_edges
    
    def degree_sequence(self):
        return sorted([len(self.adjacency_list[row]) for row in self.adjacency_list])
        
    def _get_index(self, label):
        if label not in self.vertices_map:
            raise ValueError(f"Vertex '{label}' does not exist on graph") 
        
        return self.vertices_map[label]
        
    def add_edge(self, u, v):
        try:
            self._get_index(u)
            self._get_index(v)
        except:
            print(f"Could not add Edge ({u}, {v})")
            return
        
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        self.number_edges += 1
        print(f"Edge added between {u} and {v}")
              
        
    def remove_edge(self, u, v):
        try:
            self._get_index(u)
            self._get_index(v)
        except:
            print(f"Could not remove Edge ({u}, {v})")
            
        print(f"Removing edge between {u} and {v}")
        self.adjacency_list[u].remove(v)
        self.number_edges -= 1
        
    def print_graph(self):
        if self.num_of_edges() == 0:
            print("Graph is Empty")
            return
        
        print("\nGraph Representation (Adjacency List):")
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {" ".join(map(str,neighbors))}")

    def is_simple(self):
        for vertex, neighbors in self.adjacency_list.items():
            if vertex in neighbors:
                return False
            if len(set(neighbors)) != len(neighbors):
                return False
        return True

    def is_null(self):
        return self.number_edges == 0

    def is_complete(self):
        if not self.is_simple():
            return False
        
        expected_edges = self.num_vertices * (self.num_vertices - 1) // 2
        return self.number_edges == expected_edges

# graph = DenseGraph(["A","B","C","D","E"])

# print("\n")
# graph.add_edge("A", "B")
# graph.add_edge("A", "C")
# graph.add_edge("C", "D")
# graph.add_edge("C", "E")
# graph.add_edge("B", "D")

# graph.print_graph()
# print("\n")
# print(f"Number of vertices: {graph.num_of_vertices()}")
# print(f"Number of edges: {graph.num_of_edges()}")
# print(f"Degrees Sequence: {graph.degree_sequence()}")
# print(f"Degrees Sequence: {graph.degree_sequence2()}")

# graph.remove_edge("A", "C")

# graph.print_graph()

class SparseGraph(Graph):
    def __init__(self, num_vertices_or_labels):
        self.vertices_map = {}
        self.indices_map = {}
        self.number_edges = 0
        
        if isinstance(num_vertices_or_labels, int):
            
            self.num_vertices = num_vertices_or_labels
            
            for i in range(self.num_vertices):
                self.vertices_map[i] = i
                self.indices_map[i] = i  
        elif isinstance(num_vertices_or_labels, list):
            
            self.num_vertices = len(num_vertices_or_labels)
            
            for i, label in enumerate(num_vertices_or_labels):
                
                if label in self.vertices_map:
                    raise ValueError(f"Duplicated label '{label}' in the vertex list")
                
                self.vertices_map[label] = i
                self.indices_map[i] = label
            
        else:
            raise ValueError("Argumento must be an integer number of vertices or a list of labels")
        
        self.adjacency_list = defaultdict(list) 
        
    def num_of_vertices(self):
        return self.num_vertices
    
    def num_of_edges(self):
        return self.number_edges
    
    def degree_sequence(self):
        return sorted([len(self.adjacency_list[row]) for row in self.adjacency_list])
        
    def _get_index(self, label):
        if label not in self.vertices_map:
            raise ValueError(f"Vertex '{label}' does not exist on graph") 
        
        return self.vertices_map[label]
        
    def add_edge(self, u, v):
        try:
            self._get_index(u)
            self._get_index(v)
        except:
            print(f"Could not add Edge ({u}, {v})")
            return
        
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        self.number_edges += 1
        print(f"Edge added between {u} and {v}")
                
        
    def remove_edge(self, u, v):
        try:
            self._get_index(u)
            self._get_index(v)
        except:
            print(f"Could not remove Edge ({u}, {v})")
            
        print(f"Removing edge between {u} and {v}")
        self.adjacency_list[u].remove(v)
        self.number_edges -= 1
        
    def print_graph(self):
        if self.num_of_edges == 0:
            print("Graph is Empty")
            return
        
        print("\nGraph Representation (Adjacency List):")
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {" ".join(map(str,neighbors))}")


# graph2 = SparseGraph(["A","B","C","D","E"])

# graph2.add_edge("A","B")
# graph2.add_edge("A","C")
# graph2.add_edge("A","C")
# graph2.add_edge("C","D")
# graph2.add_edge("C","E")
# graph2.add_edge("B","D")

# graph2.print_graph()

# print(f"Number of vertices: {graph2.num_of_vertices()}")
# print(f"Number of edges: {graph2.num_of_edges()}")
# print(f"Degrees Sequence: {graph2.degree_sequence()}")

# graph2.remove_edge("A","C")
# graph2.remove_edge("C","A")

# graph2.print_graph()

