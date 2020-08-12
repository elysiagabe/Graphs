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
        # create empty queue & store starting vert
        q = Queue()
        q.enqueue(starting_vertex)

        # create visited set to store visited verts
        visited_verts = set()

        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vert in queue
            current_vert = q.dequeue()

            # if vert has NOT been visited
            if current_vert not in visited_verts:
                # mark as visisted by adding to visited set
                visited_verts.add(current_vert)
                # can print for debug
                print(current_vert)

                # add each of its neighbors to the queue
                for neighbor in self.get_neighbors(current_vert):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack & store starting vert
        s = Stack()
        s.push(starting_vertex)

        # create visited set to store visited verts
        visited_verts = set()

        # while stack is not empty
        while s.size() > 0:
            # pop off the first vert
            current_vert = s.pop()

            # if vert has NOT been visited
            if current_vert not in visited_verts:
                # mark vert as visited
                visited_verts.add(current_vert)
                # can print for debug
                print(current_vert)

                # add all of it's neighbors to the top of the stack
                for neighbor in self.get_neighbors(current_vert):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited_verts=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # create visited set to store visited verts
        if visited_verts is None: 
            visited_verts = set()

        # if vertex has NOT been visited
        if starting_vertex not in visited_verts:
            # mark as visited by adding to set
            visited_verts.add(starting_vertex)
            # print vertex
            print(starting_vertex)

        # find neighbors of vertex...then call dft_recursive on each neighbor that's not currently in visited_verts (find difference b/t neighbors set and visited set)
        for neighbor in self.get_neighbors(starting_vertex) - visited_verts:
            self.dft_recursive(neighbor, visited_verts)

        '''
        CLASS SOLUTION: 

        if visited is None:
            visited = set()
        visited.add(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited)
        '''

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # initialize queue...this will need to store possible paths instead of individual nodes
        q = Queue()

        # initialize visited set
        visited_verts = set()

        # add start vert as list to queue
        q.enqueue([starting_vertex])

        # if starting vertex is destination, we're done...return
        if starting_vertex == destination_vertex:
            return q
        
        # otherwise while queue is not empty
        while q.size() > 0:
            # dequeue the first path from the queue
            path = q.dequeue()
            # get the last vertex in the path
            current_vertex = path[-1]

            # if current node has not been visited
            if current_vertex not in visited_verts:
                # mark as visited by adding to visited set
                visited_verts.add(current_vertex)
                
                # iterate over its neighbors
                for neighbor in self.get_neighbors(current_vertex):
                    # create list to contain new path (original path + neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    # enqueue new path
                    q.enqueue(new_path)

                    # if neighbor is destination, return new path
                    if neighbor == destination_vertex:
                        return new_path

        '''
        CLASS SOLUTION:
        q = Queue()
        q.enqueue([starting_vertex_id])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in visited:
                if v == target_vertex_id:
                    return path
                visited.add(v)

                for next_v in self.get_neighbors(v):
                    path_copy = list(path) # or [path]...need copy of path not a reference
                    path_copy.append(next_v)
                    q.enqueue(path_copy)

        return None
        '''



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize stack
        s = Stack()

        # initialize visited
        visited_verts = set()
        
        # add start to stack
        s.push([starting_vertex])

        # if starting vertex is destination...return
        if starting_vertex == destination_vertex:
            return starting_vertex

        # otherwise while queue is not empty: 
        while s.size() > 0:
            # pop first path from stack
            path = s.pop()
            # get the last vertex in the path
            current_vertex = path[-1]

            # if current vertex has NOT been visited: 
            if current_vertex not in visited_verts:
                # mark as visited
                visited_verts.add(current_vertex)

                # iterate over its neighbors
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    # push new path to stack
                    s.push(new_path)

                    # if neighbor is destination, return the new path
                    if neighbor == destination_vertex:
                        return new_path

    def dfs_recursive(self, starting_vertex, destination_vertex, visited_verts=set(), path_so_far=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # adds starting vertex to path_so_far
        path_so_far = path_so_far + [starting_vertex]

        # if vertex has not been visited
        if starting_vertex not in visited_verts:
            # mark as visited
            visited_verts.add(starting_vertex)

        # if start is destination, return path
        if starting_vertex == destination_vertex:
            return path_so_far

        # then iterate over neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            # if neighbor has not been visited
            if neighbor not in visited_verts:
                # call dfs_recursive
                result = self.dfs_recursive(neighbor, destination_vertex, visited_verts, path_so_far)
                # return when the result is not None
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
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
