# helper function to find parents of child node on the fly (negates need to build out a graph)
def get_ancestors(relationships, node): 
    parents = []
    for parent, child in relationships: 
        if node is child: 
            parents.append(parent)
    return parents

def earliest_ancestor(ancestors, starting_node):
    # if node has no parents, return -1
    if len(get_ancestors(ancestors, starting_node)) < 1: 
        return -1
    
    # Earliest ancestor means we're looking for the LONGEST path --> DEPTH FIRST SEARCH
    # Initialize visited set & stack to traverse
    visited = set()
    stack = []
    stack.append([starting_node])

    # Initialize longest_path array
    longest_path = []

    # Traverse graph
    while len(stack) > 0: 
        current_path = stack.pop()

        # if current_path is longer than the longest_path OR if they're the same length and current path's earliest ancestor has a lower numerical value than that of longest_path, update longest_path to current_path
        if len(current_path) > len(longest_path) or len(current_path) == len(longest_path) and current_path[-1] < longest_path[-1]:
            longest_path = current_path

        current_node = current_path[-1]

        if current_node not in visited: 
            visited.add(current_node)

            for parent in get_ancestors(ancestors, current_node):
                new_path = list(current_path)
                new_path.append(parent)
                stack.append(new_path)

    # after traversing the graph, earliest ancestor will be the last value in the longest_path list
    earliest_ancestor = longest_path[-1]
    return earliest_ancestor


