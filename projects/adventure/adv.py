from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

print("num of rooms:", len(world.rooms))

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Contruct a traversal graph...
# traversal_graph = {
#     0: {
#         n: '?',
#         s: '?',
#         e: '?',
#         w: '?'
#     },
#     1: {
#         n: '?', s: '?', e: '?', w: '?'
#     },
#     2: {
#         n: '?', s: '?', e: '?', w: '?'
#     },
# } 

traversal_graph = {}
for i in range(0, len(world.rooms)):
    traversal_graph[i] = {}

def are_we_done():
    if len(traversal_graph) <= len(world.rooms):
        return False
    visited_rooms = traversal_graph.keys()
    for room in visited_rooms:
        if "?" in traversal_graph[room].values():
            return False
    return True

def find_nearest_unexplored(current_room_id): 
    # visited = {}
    visited = set()
    room_queue = []
    
    next_directions_queue = []
    room_queue.append([current_room_id])
    print("Q:", room_queue)

    while len(room_queue) > 0: 
        current_path = room_queue.pop(0)
        current_room = current_path[-1]

        if current_room not in visited:
            # look for an exit with ? as a value
            if "?" in traversal_graph[current_room].values():
                print("visited: ", visited, "Current room: ", current_room, "Current path: ", current_path)

                print("next directions queue:", next_directions_queue)
                # for direction in next_directions_queue:
                #     player.travel(direction)
                #     traversal_path.append(direction)
                
                return next_directions_queue
            # visited[current_room] = current_path
            visited.add(current_room)

            for direction, room in traversal_graph[current_room].items():
                if room not in visited:
                    print("Direction: ", direction, "Room: ", room)

                    next_path = list(current_path)
                    next_path.append(room)
                    room_queue.append(next_path)
                    next_directions_queue.append(direction)
                    # player.travel(direction)
                    # traversal_path.append(direction)
        #             for step in next_steps: 
        # print("step", step)
        # player.travel(step)
        # traversal_path.append(step)
        
    return []
    # print("visited: ", visited)

# put current room and its exits in traversal graph
get_opposite = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e',
}

traversal_graph[player.current_room.id] = {direction: '?' for direction in player.current_room.get_exits()}
# print("Traversal Graph:", traversal_graph)

# DEPTH FIRST TRAVERSAL
# initialize a stack
s = []
s.append(player.current_room.id)
# keep track of visited rooms
visited_rooms = set()

while not are_we_done():
    if len(s) == 0:
        break
    print("are we done?", are_we_done())
    print("stack:", s)
    print("visited rooms:", visited_rooms)
    print("Traversal Graph:", traversal_graph)
    current_room = s.pop()
    exits = player.current_room.get_exits()

    if current_room not in visited_rooms:
        visited_rooms.add(current_room)
        for exit in exits: 
            if exit not in traversal_graph[current_room].keys():
                traversal_graph[current_room][exit] = '?'


    next_direction = None
    for direction, room in traversal_graph[current_room].items():
        if room is '?':
            next_direction = direction
    
    if next_direction:
        print("next direction: ", next_direction)
        # player moves to the room in the next direction...
        player.travel(next_direction)
        traversal_path.append(next_direction)
        # add next_room to stack to visit...
        next_room = player.current_room.id
        # update the previous (current) room with direction value of next room...
        traversal_graph[current_room][next_direction] = next_room
        traversal_graph[next_room][get_opposite[next_direction]] = current_room
        s.append(next_room)
    else: 
        # when no more directions to explore, find next room with an unexplored direction
        current_room = player.current_room.id
        next_steps = find_nearest_unexplored(current_room)
        print("** NEXT STEPS**", next_steps)
        print("TRAVERSAL PATH::::1 ", traversal_path) 
        if len(next_steps) == 0:
            break  
        for step in next_steps:
            print("step", step)
            player.travel(step)
            traversal_path.append(step)   
        s.append(player.current_room.id)
        print("TRAVERSAL PATH:::: ", traversal_path)     
        


# print("Current room: ", player.current_room.id)
# print("Exit: ", player.current_room.get_exits())
# print("Travel: ", player.travel('n'))
# print("Current room: ", player.current_room.id)


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
