elevation_map = open("day12_input.txt","r").read().split("\n")
test_map = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi'''.split("\n")

elevations = {
    "a": 1, 
    "b": 2, 
    "c": 3, 
    "d": 4, 
    "e": 5, 
    "f": 6, 
    "g": 7, 
    "h": 8, 
    "i": 9, 
    "j": 10, 
    "k": 11, 
    "l": 12, 
    "m": 13, 
    "n": 14, 
    "o": 15, 
    "p": 16, 
    "q": 17, 
    "r": 18,
    "s": 19, 
    "t": 20, 
    "u": 21, 
    "v": 22, 
    "w": 23, 
    "x": 24,
    "y": 25,
    "z": 26, 
    "E": 26, # end point is elevation z
    "S": 1, # start point is elevation a
}

# first some setup:
def find_square(data_map,square):
    # square will be "S" or "E"
    for i in range(len(data_map)):
        if square in data_map[i]:
            square_y = i
            square_x = data_map[i].index(square)
            return square_x,square_y

def get_starting_stats(data_map):
    unvisited_squares = set()
    tentative_distances = dict()
    for x,y in [(x,y) for x in range(len(data_map[0])) for y in range(len(data_map))]:
        # unvisited squares
        unvisited_squares.add((x,y))
        # tentative_distances
        if data_map[y][x] == "S":
            tentative_distances[(x,y)] = 0
        else: tentative_distances[(x,y)] = 999999 # big number
    return unvisited_squares,tentative_distances

# now some useful functions            

def elevation(data_map,square):
    # square is an (x,y) pair
    return elevations[data_map[square[1]][square[0]]]

def is_valid_move(data_map,current,destination):
    # current and destination as (x,y) pairs
    return elevation(data_map,destination) <= elevation(data_map,current) + 1


# actual algorithm code

def get_shortest_path(data_map):
    starting_square = find_square(data_map,"S")
    ending_square = find_square(data_map,"E")
    unvisited_squares,tentative_distances = get_starting_stats(data_map)
    
    current_square = starting_square
    
    while True:
        current_x = current_square[0]; current_y = current_square[1]
        #get neighbors
        neighbors = [
            (current_x,current_y - 1), #up
            (current_x,current_y + 1), #down
            (current_x - 1,current_y), #left
            (current_x + 1,current_y), #right
        ]
        # calculate tentative distances :')
        for neighbor in neighbors:
            neighbor_x = neighbor[0]; neighbor_y = neighbor[1]
            # if outside of map, skip
            if neighbor_x < 0 or neighbor_y < 0 or neighbor_x >= len(data_map[0]) or neighbor_y >= len(data_map): continue
            # if not a valid move, skip
            if not is_valid_move(data_map,current_square,neighbor): continue
            
            new_distance = tentative_distances[current_square] + 1
            if new_distance < tentative_distances[neighbor]: 
                tentative_distances[neighbor] = new_distance
        #clean-up
        unvisited_squares.remove(current_square)
        if ending_square not in unvisited_squares: break
        #next square:
        current_square = sorted(list(unvisited_squares),key=lambda x: tentative_distances[x])[0]
    
    return tentative_distances[ending_square] #:')

print("Test:")
print(f'The shortest path is {get_shortest_path(test_map)} steps')
print("Real:")
print(f'The shortest path is {get_shortest_path(elevation_map)} steps')

