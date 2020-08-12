
def earliest_ancestor(ancestors, starting_node):
    # initialize graph
    graph = {}

    # build out graph...ancestors is made up of pairs of (parent, child)...in the graph, vertex/key will be child and edge/value will be parent
    for parent, child in ancestors: 
        if child not in graph: 
            graph[child] = {parent}
        else: 
            graph[child].add(parent)

    # initialize stack to keep track of paths
    stack = []
    # append starting node to stack
    stack.append([starting_node])

    # initialize visited set to keep track of visited verts
    visited = set()

    # initialize longest path -- we are looking for longest path -- earliest ancestor will be the last item in the longest path
    longest_path = []

    # DFS
    while len(stack) > 0: 
        # pop path off stack
        current_path = stack.pop()
        # current vert is last in path
        current_vert = current_path[-1]

        # update longest path if current path is longer OR if they're the same length and current path's earliest ancestor (last in list) is less than that of longest
        if (len(current_path) == len(longest_path) and current_path[-1] < longest_path[-1]) or len(current_path) > len(longest_path):
            longest_path = current_path

        # if current vert has NOT been visited
        if current_vert not in visited:
            # mark as visited
            visited.add(current_vert)

            # only do the following if current vert has parents (i.e., if child/key exists in graph)
            if current_vert in graph:
                # iterate thru parents and create new path, append to stack
                for parent in graph[current_vert]: 
                    new_path = list(current_path)
                    new_path.append(parent)
                    stack.append(new_path)

    # if the starting node is the same as the earliest ancestor (i.e., last in path)
    if starting_node == longest_path[-1]:
        # return -1 
        return -1
    else: 
        # otherwise return earliest ancestor (i.e., last vert in longest path)
        return longest_path[-1]