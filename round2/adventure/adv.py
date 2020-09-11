from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
~~~~~~~~~~~~~~~~~~~
MY CODE STARTS HERE
~~~~~~~~~~~~~~~~~~~
'''

opposite_dir = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}

# INITIALIZE A TRAVERSAL GRAPH
traversal_graph = {}
for room in world.rooms: 
    traversal_graph[room] = {}
    exits = world.rooms[room].get_exits()
    traversal_graph[room] = {ex: '?' for ex in exits}

# Function to check if we're done...returns True if there are no ?s...used to break while loop
def are_we_done():
    for room in traversal_graph.keys():
        if "?" in traversal_graph[room].values():
            return False
    return True

# initialize a stack for traversal
s = []
# add current room to stack
s.append(player.current_room.id)
# initialize path array...will be used in case we need to backtrack
path = []

while not are_we_done():
    # if there's nothing in the stack, break
    if len(s) == 0:
        break
    
    # this is the current room player is in
    current_room = s.pop()
    # initialize next_direction variable
    next_direction = None

    # is there an unexplored exit, i.e., a question mark? if so, that's the next direction we want to explore
    for direction, room in traversal_graph[current_room].items():
        if room is '?': 
            next_direction = direction

    # if next direction is not None, travel in that direction...keep track of where you're going
    if next_direction: 
        player.travel(next_direction)
        traversal_path.append(next_direction)
        path.append(next_direction)

        next_room = player.current_room.id

        # update the traversal graph to keep track of where you've been 
        traversal_graph[current_room][next_direction] = next_room
        traversal_graph[next_room][opposite_dir[next_direction]] = current_room

        # add the next room to the stack to keep traversing
        s.append(next_room)

    # if you've reached the end of the path, i.e., no unexplored directions (no question marks)
    else: 
        if "?" not in traversal_graph[player.current_room.id].values():
            # backtrack to the previous room you were in and check if there's any other exits to explore
            last_direction = opposite_dir[path.pop()]
            player.travel(last_direction)
            traversal_path.append(last_direction)
        
        # add the room you backtracked to to the stack to keep traversing
        s.append(player.current_room.id)


'''
~~~~~~~~~~~~~~~~~~~
MY CODE ENDS HERE
~~~~~~~~~~~~~~~~~~~
'''

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
