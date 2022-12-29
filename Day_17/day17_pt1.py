

# Falling rocks:
#              #          #       #
#  ####  -->  ###  -->    #  -->  #  -->  ##
#              #        ###       #       ##
#                                 #

# ground is 0, y is higher, higher up, x is higher to the right

# seven units wide
# #.......#
# #########

class Rock:
    def __init__(self,rock_type,x,y):
        # x,y are the bottom left corner, not necessarily a point on the rock
        self.x = x
        self.y = y
        self.type = rock_type # 1, 2, 3, 4, or 5
        self.blocks = self.get_blocks() #list

    def get_blocks(self):
        #### FIX
        # x,y are the bottom left corner, not necessarily a point on the rock
        # returns list
        blocks = [(self.x,self.y)]
        if self.type == 1: # line shape
            # self.x and self.y are left-most point
            blocks += [
                (self.x+1,self.y),
                (self.x+2,self.y),
                (self.x+3,self.y)
            ]
        elif self.type == 2: # plus sign shape
            # self.x and self.y are left-most point
            bloks += [
                (self.x+1,self.y),
                (self.x+2,self.y),
                (self.x+1,self.y+1),
                (self.x+1,self.y-1)
            ]
        elif self.type == 3: # backwards L shape
            # self.x and self.y are left-most point
            blocks += [
                (self.x+1,self.y),
                (self.x+2,self.y),
                (self.x+2,self.y+1),
                (self.x+2,self.y+2),
            ]
        elif self.type == 4: # I shape
            # self.x and self.y are top-most point
            blocks += [
                (self.x,self.y-1),
                (self.x,self.y-2),
                (self.x,self.y-3)
            ]
        elif self.type == 5: # square shape
            # self.x and self.y are left-most and top-most point
            blocks += [
                (self.x+1,self.y),
                (self.x,self.y+1),
                (self.x+1,self.y+1)
            ]
        return blocks

        def move(self,dir):
            if dir == '>': self.x += 1
            elif dir == '<': self.x -= 1
            self.blocks = self.get_blocks()

        def fall(self):
            self.y+=1
            self.blocks = self.get_blocks()

class Cave:
    def __init__(self):
        self.width = 7
        self.floor = 0 # floor is at y=0
        self.rock_height = 0 # total height of stacked rocks
        self.rocks = []
        self.rock_counter = 1 #goes 1,2,3,4,5 - determines which rock falls

    def drop_rock(self):
        rock_type = self.rock_counter%5
        if rock_type == 0: rock_type = 5  # 0 => rock type 5
        x = 3 #(most of the time??)
        y = self.rock_height + 3

        rock = Rock(rock_type,x,self.rock_height+3)


# its left edge is two units away from the left wall

def move(x,dir):
    if dir == '>': x += 1
    elif dir == '<': x -= 1
    return x

def fall(y):
    return y+=1
