"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else: 
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Initialize an empty queue
        q = Queue();
        # Add starting_vertex to queue
        q.enqueue(starting_vertex)
        # Initialize set for visited verts
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # Dequeue node
            v = q.dequeue()
            # If node has NOT been visited
            if v not in visited:
                # if not, add to visited set
                visited.add(v)
                print(v)
                # then enqueue its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Initialize stack
        s = Stack()
        # Push starting vert to stack
        s.push(starting_vertex)
        # Initialize visited set
        visited = set()
        # While stack is not empty
        while s.size() > 0: 
            # Pop off vert from stack
            v = s.pop()
            # If vert has NOT been visited
            if v not in visited: 
                # Mark as visited
                visited.add(v)
                print(v)
                # Add neighbors to stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Initialize visited as empty set ONLY ONCE
        if visited is None: 
            visited = set()
        # Add starting_vertex to visited
        visited.add(starting_vertex)
        print(starting_vertex)

        # For each of starting_vertex's neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            # If neighbor has not been visited yet
            if neighbor not in visited:
                # Call dft_recursive on it...pass in neighbor and visited
                self.dft_recursive(neighbor, visited)



    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Initialize an empty queue 
        q = Queue()
        # Enqueue PATH to the starting_vertex
        q.enqueue([starting_vertex])
        # Initialize visited set
        visited = set()

        # While the queue is NOT empty: 
        while q.size() > 0: 
            # Dequeue the first PATH
            current_path = q.dequeue()
            # Grab the last vertex from the dequeued path
            current_vert = current_path[-1]
            # If that vertex ahs NOT been visited
            if current_vert not in visited: 
                # Check if it's the target
                if current_vert is destination_vertex: 
                    # If it is: RETURN THE PATH
                    return current_path
                # Mark vert as visited
                visited.add(current_vert)
                # Add Paths w/it's neighbors to back of queue
                for neighbor in self.get_neighbors(current_vert):
                    # COPY PATH
                    new_path = list(current_path)
                    # APPEND NEIGHBOR TO END OF COPIED PATH
                    new_path.append(neighbor)
                    # Enqueue the new path
                    q.enqueue(new_path)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Initialize stack
        s = Stack()
        # Push starting vertex as a path list to stack
        s.push([starting_vertex])
        # Initialize visited set
        visited = set()

        # While stack is not empty
        while s.size() > 0:
            # Pop the first PATH from the stack
            current_path = s.pop()
            # Grab the last vertex from the PATH
            current_vert = current_path[-1]
            # If that vertex has NOT been visited
            if current_vert not in visited: 
                # Check if it's the target
                if current_vert is destination_vertex:
                    # if it is, RETURN THAT PATH
                    return current_path
                # Mark vert as visited
                visited.add(current_vert)
                # Add paths that include neighbors to stack
                for neighbor in self.get_neighbors(current_vert):
                    # Copy path
                    new_path = list(current_path)
                    # Append neighbor to end of copied path
                    new_path.append(neighbor)
                    # Push new path to stack
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), current_path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # add starting vertex to end of path
        current_path = current_path + [starting_vertex]

        # if starting vert has NOT been visited
        if starting_vertex not in visited: 
            # mark as visited
            visited.add(starting_vertex)

        # if starting vert is destination
        if starting_vertex is destination_vertex: 
            # return the path
            return current_path

        # for each of starting vert's neighbors
        for neighbor in self.get_neighbors(starting_vertex): 
            # if the neighbor hasn't been visited
            if neighbor not in visited:                 
                # call dfs_recursive
                result = self.dfs_recursive(neighbor, destination_vertex, visited, current_path)
                # if the result is not None, return it
                if result is not None: 
                    return result 

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))