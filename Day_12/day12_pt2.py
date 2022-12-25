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

def get_starting_squares(data_map):
    starting_squares = set()
    for y in range(len(data_map)):
        for x in range(len(data_map[0])):
            if data_map[y][x] == 'S' or data_map[y][x] == 'a':
                starting_squares.add((x,y))
    return starting_squares

def find_square(data_map,square):
    # square will be "S" or "E"
    for i in range(len(data_map)):
        if square in data_map[i]:
            square_y = i
            square_x = data_map[i].index(square)
            return square_x,square_y

def get_starting_stats(data_map,starting_square):
    unvisited_squares = set()
    tentative_distances = dict()
    for x,y in [(x,y) for x in range(len(data_map[0])) for y in range(len(data_map))]:
        # unvisited squares
        unvisited_squares.add((x,y))
        # tentative_distances
        if (x,y) == starting_square:
            tentative_distances[(x,y)] = 0
        else: tentative_distances[(x,y)] = float('inf') # big number
    return unvisited_squares,tentative_distances

# now some useful functions            

def elevation(data_map,square):
    # square is an (x,y) pair
    return elevations[data_map[square[1]][square[0]]]

def is_valid_move(data_map,current,destination):
    # current and destination as (x,y) pairs
    return elevation(data_map,destination) >= elevation(data_map,current) - 1

def get_neighbors(square):
    # square is an (x,y) pair
    return [
            (square[0],square[1] - 1), #up
            (square[0],square[1] + 1), #down
            (square[0] - 1,square[1]), #left
            (square[0] + 1,square[1]), #right
            ]
def is_outside(data_map,square):
    return square[0] < 0 or square[1] < 0 or square[0] >= len(data_map[0]) or square[1] >= len(data_map)

def get_lowest_unvisited(unvisited_squares,tentative_distances):
    return sorted(list(unvisited_squares),key=lambda x: tentative_distances[x])[0]

# actual algorithm code

def get_shortest_path(data_map):
    # we'll go backwards from the end
    end_square = find_square(data_map,"E")
    unvisited_squares,tentative_distances = get_starting_stats(data_map,end_square)
    
    current_square = end_square
    
    while True:
        #get neighbors
        neighbors = get_neighbors(current_square)
        # calculate tentative distances :')
        for neighbor in neighbors:
            # if outside of map or invalid move, skip
            if is_outside(data_map,neighbor) or not is_valid_move(data_map,current_square,neighbor): continue
            # calculate new tentative distance
            new_distance = tentative_distances[current_square] + 1
            if new_distance < tentative_distances[neighbor]: 
                tentative_distances[neighbor] = new_distance
        #mark current square as visited and check if we've visited ending_square
        unvisited_squares.remove(current_square)
        #next square is unvisited square with shortest tentative distance
        if len(unvisited_squares) == 0: break
        current_square = get_lowest_unvisited(unvisited_squares,tentative_distances)
        # if lowest tentative distance of unvisited square is inf, end here
        if not tentative_distances[current_square] < float('inf'): break
        #current_square = sorted(list(unvisited_squares),key=lambda x: tentative_distances[x])[0]
    closest_a = sorted(get_starting_squares(data_map),key=lambda x: tentative_distances[x])[0]
    return tentative_distances[closest_a] #:')

def shortest_past_of_all_starts(data_map):
    starting_squares = get_starting_squares(data_map)
    end_square = find_square(data_map,"E")
    
    shortest_paths = []
    for start_square in starting_squares:
        shortest_paths.append(get_shortest_path(data_map,start_square,end_square))
    
    return min(shortest_paths)

#print('### pt1 ###')
#print("Test:")
#print(f'The shortest path is {get_shortest_path(test_map,find_square(test_map,"S"),find_square(test_map,"E"))} steps')
#print("Real:")
#print(f'The shortest path is {get_shortest_path(elevation_map,find_square(elevation_map,"S"),find_square(elevation_map,"E"))} steps')

print('### pt2 ###')
print("Test:")
print(f'The shortest path is {get_shortest_path(test_map)} steps')
print("Real:")
print(f'The shortest path is {get_shortest_path(elevation_map)} steps')
