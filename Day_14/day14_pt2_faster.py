# sand movement:
# drops from 500,0
#  1. go down
#  2. if can't go down, do left down (diag)
#  3. if can't go left down (diag), go right down (diag)
#  4. if can't go right down (diag), comes to rest

def format_input(input_file):
    return [path.split(" -> ") for path in open(input_file,"r").read().split("\n")]

def get_rocks(input_file):
    cave_slice = format_input(input_file)
    rocks = []; horizontal_rocks = []
    for path in cave_slice:
        for vertex in range(len(path) - 1):
            current_x,current_y = list(map(int,path[vertex].split(",")))
            next_x,next_y = list(map(int,path[vertex+1].split(",")))
            if not current_x == next_x:
                # get horizontal rockkk:
                horizontal_rocks.append([(current_x,current_y),(next_x,next_y)])
                if current_x < next_x: lower = current_x; higher = next_x
                else: lower = next_x; higher = current_x
                for x in range(lower,higher+1):
                    rocks.append((x,current_y))
            elif not current_y == next_y:
                if current_y < next_y: lower = current_y; higher = next_y
                else: lower = next_y; higher = current_y
                for y in range(lower,higher+1):
                    rocks.append((current_x,y))
    return list(set(rocks)),horizontal_rocks


##### FIRST WE NEED THE SIZE OF THE TRIANGLE #####

test_rocks,test_horizontal_rocks = get_rocks("day14_test_input.txt")
source = (500,0)
floor = max(test_rocks,key=lambda i:i[1])[1] + 2

# sum of first m odd numbers is m^2
most_possible_sand = floor*floor

print("Triangle:",most_possible_sand)

### SUBTRACT ROCKS ###
number_of_rocks = len(set(test_rocks))

sand_without_rocks = most_possible_sand - number_of_rocks

print("Without rocks:",sand_without_rocks)

### SUBTRACT EMPTY SPACE ###

# how do we even calculate the empty space :'(
print(test_horizontal_rocks)


#print("### pt1 ###")
#print("test:")
#print(f"\n\nYou will see {pt2(format_input('day14_test_input.txt'))} sand pieces before there's running sand.")
#print("real:")
#print(f"\n\nYou will see {pt2(format_input('day14_input.txt'))} sand pieces before there's running sand.")
