# sand movement:
# drops from 500,0
#  1. go down
#  2. if can't go down, do left down (diag)
#  3. if can't go left down (diag), go right down (diag)
#  4. if can't go right down (diag), comes to rest

def format_input(input_file):
    return [path.split(" -> ") for path in open(input_file,"r").read().split("\n")]

def get_rocks(cave_slice):
    rocks = []
    for path in cave_slice:
        for vertex in range(len(path) - 1):
            current_x,current_y = list(map(int,path[vertex].split(",")))
            next_x,next_y = list(map(int,path[vertex+1].split(",")))
            if not current_x == next_x:
                if current_x < next_x: lower = current_x; higher = next_x
                else: lower = next_x; higher = current_x
                for x in range(lower,higher+1):
                    rocks.append((x,current_y))
            elif not current_y == next_y:
                if current_y < next_y: lower = current_y; higher = next_y
                else: lower = next_y; higher = current_y
                for y in range(lower,higher+1):
                    rocks.append((current_x,y))
    return rocks

class Sand:
    def __init__(self):
        self.source = (500,0)
        self.current_tile = (500,0)
        self.state = "dropping" #states can be: dropping, running, settled
    
    def drop(self,cave):
        if not self.state == "dropping": return
        # check if we're just running sand now
        if not cave.are_lower_rocks(self.current_tile[1]):
            self.state = "running"; return
        # try down
        dest_tile = (self.current_tile[0],self.current_tile[1]+1)
        if dest_tile not in cave.rocks and dest_tile not in cave.sand_tiles:
            self.current_tile = dest_tile
            return
        # try left down (diag)
        dest_tile = (self.current_tile[0]-1,self.current_tile[1]+1)
        if dest_tile not in cave.rocks and dest_tile not in cave.sand_tiles:
            self.current_tile = dest_tile
            return
        # try right down (diag)
        dest_tile = (self.current_tile[0]+1,self.current_tile[1]+1)
        if dest_tile not in cave.rocks and dest_tile not in cave.sand_tiles:
            self.current_tile = dest_tile
            return
        # settle down
        self.state = "settled"
    
    def __str__(self):
        if self.state == "dropping": return "+"
        elif self.state == "running": return "~"
        elif self.state == "settled": return "o"

class Cave:
    def __init__(self,cave_slice):
        self.rocks = get_rocks(cave_slice)
        self.sand_objects = []
        self.sand_tiles = []
        self.sand_counter = 0
    
    def drop_sand(self):
        self.sand_objects.append(Sand())
        self.sand_counter+=1
        sand_pellet = self.sand_objects[self.sand_counter-1]
        self.sand_tiles.append(sand_pellet.current_tile)
        #if self.sand_counter%50 == 0: print(self) # for troubleshooting
        #print("\nSAND COUNTER: ",self.sand_counter) # for troubleshooting
        #print("    dropping sand",end="") # for troubleshooting
        while True:
            #print(" .",end="") # for troubleshooting
            sand_pellet.drop(self)
            self.sand_tiles[self.sand_counter-1] = sand_pellet.current_tile
            if sand_pellet.state == "running":
                return "running"
            if sand_pellet.state == "settled":
                return "settled"
    
    def fill_up(self):
        while True:
            if self.drop_sand() == "running":
                return self.sand_counter - 1
    
    def are_lower_rocks(self,y_coord):
        if y_coord < self.get_max_xy()[1]:
            return True
        else: return False 
    
    def get_min_xy(self):
        obstacles = self.rocks + self.sand_tiles
        x = min(obstacles,key=lambda i:i[0])[0]
        y = min(obstacles,key=lambda i:i[1])[1]
        return (x,y)
    
    def get_max_xy(self):
        obstacles = self.rocks + self.sand_tiles
        x = max(obstacles,key=lambda i:i[0])[0]
        y = max(obstacles,key=lambda i:i[1])[1]
        return (x,y)
    
    def __str__(self):
        min_pair = self.get_min_xy()
        max_pair = self.get_max_xy()
        #print("\nStart") # for debugging
        for y in range(min_pair[1],max_pair[1]+1):
            row = ""
            for x in range(min_pair[0],max_pair[0]+1):
                if (x,y) in self.rocks:
                    row+="#"
                elif (x,y) == (500,0): # sand source
                    row +="+"
                elif (x,y) in self.sand_tiles:
                    sand = self.sand_objects[self.sand_tiles.index((x,y))]
                    row += str(sand)
                else: row += "."
            print(row)
        return ""

def pt1(cave_slice):
    cave = Cave(cave_slice)
    sand_needed = cave.fill_up()
    print(cave) # for visualization
    return sand_needed

print("### pt1 ###")
print("test:")
print(f"\n\nYou will see {pt1(format_input('day14_test_input.txt'))} sand pieces before there's running sand.")
print("real:")
print(f"\n\nYou will see {pt1(format_input('day14_input.txt'))} sand pieces before there's running sand.")
