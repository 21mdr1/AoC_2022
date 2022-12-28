

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
        self.x = x
        self.y = y
        self.type = rock_type # 1, 2, 3, 4, or 5
        self.blocks = self.get_blocks() #list

    def get_blocks(self):
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

def move(x,dir):
    if dir == '>': x += 1
    elif dir == '<': x -= 1
    return x

def fall(y):
    return y+=1
