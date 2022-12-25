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

class Rope:
    def __init__(self,head,tail):
        # in x,y coordinates
        self.head_x = int(head[0])
        self.head_y = int(head[2])
        self.tail_x = int(tail[0])
        self.tail_y = int(tail[2])
        self.tail_placements = {tail}
    
    def up(self,steps):
        for i in range(steps):
            self.head_y += 1
            if not self.head_and_tail_are_touching():
                self.move_tail()
    
    def down(self,steps):
        for i in range(steps):
            self.head_y -= 1
            if not self.head_and_tail_are_touching():
                self.move_tail()
    
    def left(self,steps):
        for i in range(steps):
            self.head_x -= 1
            if not self.head_and_tail_are_touching():
                self.move_tail()
        
    def right(self,steps):
        for i in range(steps):
            self.head_x += 1
            if not self.head_and_tail_are_touching():
                self.move_tail()
    
    def head_and_tail_are_touching(self):
        if abs(self.head_x - self.tail_x) <= 1 and abs(self.head_y - self.tail_y) <= 1:
            return True
        else: return False
    
    def move_tail(self):
        if self.tail_x > self.head_x:
            self.tail_x -= 1
        elif self.tail_x < self.head_x:
            self.tail_x += 1
        if self.tail_y > self.head_y:
            self.tail_y -= 1
        elif self.tail_y < self.head_y:
            self.tail_y += 1
        tail_placement = str(self.tail_x) + "," + str(self.tail_y)
        self.record_tail_placement(tail_placement)
    
    def record_tail_placement(self,placement):
        self.tail_placements.add(placement)
    
    def __str__(self):
        #visualizing current state
        x_boundary = max(self.head_x,self.tail_x,10)
        y_boundary = max(self.head_y,self.tail_y,10)
        
        empty = '.'
        head = 'H'
        tail = 'T'
        
        for y in reversed(range(1,y_boundary)):
            row = ''
            for x in range(1,x_boundary):
                if self.head_x == x and self.head_y == y:
                    row += head
                elif self.tail_x == x and self.tail_y == y:
                    row += tail
                else: row += empty
            print(row)
        return ''


rope = Rope("1,1","1,1")

go = {
    "U": rope.up,
    "D": rope.down,
    "L": rope.left,
    "R": rope.right,
}

def get_tail_journey(data,visualize):
    for row in data:
        if visualize: print("==",row,"==")
        direction,steps = row.split()
        go[direction](int(steps))
        if visualize: print(rope)
    print(f"The number of places the tail has been in is: {len(rope.tail_placements)}")

#get_tail_journey(test_data,False)
get_tail_journey(real_data,False)
