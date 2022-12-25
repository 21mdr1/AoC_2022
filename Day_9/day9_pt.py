real_data = open("day9_input.txt","r").read().split("\n")

test_data = [
    'R 4',
    'U 4',
    'L 3',
    'D 1',
    'R 4',
    'D 1',
    'L 5',
    'R 2'
]

test_data_2 = [
    'R 5',
    'U 8',
    'L 8',
    'D 3',
    'R 17',
    'D 10',
    'L 25',
    'U 20'
]

class Rope:
    def __init__(self,head,knots):
        self.myvars=vars()
        # in x,y coordinates
        # knots is a list of coordinates
        self.head_x,self.head_y = list(map(int,head.split(",")))
        #make a variable k_#_x and k_#_y for each know 1-9
        self.knots_x = [int(knot[0]) for knot in knots]
        self.knots_y = [int(knot[2]) for knot in knots]
        self.tail_placements = {knots[-1]}
    
    def move(self,direction,steps):
        for step in range(steps):
            if direction == "U": self.head_y += 1
            elif direction == "D": self.head_y -= 1
            elif direction == "L": self.head_x -= 1
            elif direction == "R": self.head_x += 1
            for i in range(len(self.knots_x)):
                if not self.are_touching(i,i+1):
                    self.move_knot(i+1)

    def are_touching(self,knot_1,knot_2):
        if knot_1 == 0: 
            if abs(self.head_x - self.knots_x[knot_2-1]) <= 1 and abs(self.head_y - self.knots_y[knot_2-1]) <= 1:
                return True
            else: return False
        if abs(self.knots_x[knot_1-1] - self.knots_x[knot_2-1]) <= 1 and abs(self.knots_y[knot_1-1] - self.knots_y[knot_2-1]) <= 1:
            return True
        else: return False
    
    def move_knot(self,knot):
        #knot is just a number
        if knot == 1:
            if self.knots_x[knot-1] > self.head_x:
                self.knots_x[knot-1] -= 1
            elif self.knots_x[knot-1] < self.head_x:
                self.knots_x[knot-1] += 1
            if self.knots_y[knot-1] > self.head_y:
                self.knots_y[knot-1] -= 1
            elif self.knots_y[knot-1] < self.head_y:
                self.knots_y[knot-1] += 1
        
        else: 
            if self.knots_x[knot-1] > self.knots_x[knot-2]:
                self.knots_x[knot-1] -= 1
            elif self.knots_x[knot-1] < self.knots_x[knot-2]:
                self.knots_x[knot-1] += 1
            if self.knots_y[knot-1] > self.knots_y[knot-2]:
                self.knots_y[knot-1] -= 1
            elif self.knots_y[knot-1] < self.knots_y[knot-2]:
                self.knots_y[knot-1] += 1
        if knot == len(self.knots_x):
            tail_placement = str(self.knots_x[knot-1]) + "," + str(self.knots_y[knot-1])
            self.record_tail_placement(tail_placement)
    
    def record_tail_placement(self,placement):
        self.tail_placements.add(placement)
    
    def __str__(self):
        #visualizing current state
        x_pos_boundary = max(self.head_x,max(self.knots_x),10)
        x_neg_bounday = min(self.head_x,min(self.knots_x),-10)
        y_pos_boundary = max(self.head_y,max(self.knots_y),10)
        y_neg_boundary = min(self.head_y,min(self.knots_y),-10)
        
        empty = '.'
        head = 'H'
        
        #print(self.head_x,self.head_y)
        for y in reversed(range(y_neg_boundary,y_pos_boundary+1)):
            row = ''
            for x in range(x_neg_bounday,x_pos_boundary+1):
                next_char = ''
                for i in reversed(range(1,len(self.knots_x)+1)):
                    if self.knots_x[i-1] == x and self.knots_y[i-1] == y:
                        next_char = str(i)
                if self.head_x == x and self.head_y == y:
                    next_char = head
                if next_char == '': next_char = empty
                row += next_char
            print(row)
        return ''

rope_pt1 = Rope("1,1",["1,1"])
rope_pt2 = Rope("1,1",["1,1","1,1","1,1","1,1","1,1","1,1","1,1","1,1","1,1"])

def pt1_get_tail_journey(data,visualize):
    for row in data:
        if visualize: print("==",row,"==")
        direction,steps = row.split()
        #go[direction](int(steps))
        rope_pt1.move(direction,int(steps))
        if visualize: print(rope_pt1)
    print(f"Pt 1: The number of places the tail has been in is: {len(rope_pt1.tail_placements)}")


def pt2_get_tail_journey(data,visualize):
    for row in data:
        if visualize: print("==",row,"==")
        direction,steps = row.split()
        rope_pt2.move(direction,int(steps))
        if visualize: print(rope_pt2)
    print(f"Pt 2: The number of places the tail has been in is: {len(rope_pt2.tail_placements)}")

#pt1_get_tail_journey(test_data,True)
pt1_get_tail_journey(real_data,False)

pt2_get_tail_journey(real_data,False)
#pt2_get_tail_journey(test_data,True)
#pt2_get_tail_journey(test_data_2,True)
