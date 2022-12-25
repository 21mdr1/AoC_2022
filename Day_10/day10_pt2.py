instructions = open("day10_input.txt", "r").read().split("\n")
test_data = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''.split("\n")

class CRT:
    def __init__(self,instructions):
        self.instructions = instructions
        self.cycle = 1
        self.X = 1
        self.signal_strength = self.cycle*self.X
        self.total_signal_strength = 0
        self.sprite_position = self.X - 1
        self.screen = []
        
    def check_cycle(self):
        if self.cycle%40 == 20: #if we're at one of the special cycles
            self.total_signal_strength += self.cycle*self.X
    
    def draw_pixel(self):
        x_pos = (self.cycle - 1)%40
        y_pos = (self.cycle - 1)//40
        # make new row if necessary
        if x_pos == 0: self.screen.append([''])
        #decide what to draw
        if abs(x_pos - self.X) <= 1:
            self.screen[y_pos] += '#'
        else: self.screen[y_pos] += '.'
        
    def start_cycle(self):
        self.draw_pixel()
        
    def end_cycle(self):
        self.cycle+=1
        self.check_cycle()
        self.sprite_position = self.X - 1
    
    def addx(self,V):
        #cycle 1
        self.start_cycle()
        self.end_cycle()
        #cycle 2
        self.start_cycle()
        self.X+=V
        self.end_cycle()

    def noop(self):
        # cycle 1
        self.start_cycle()
        self.end_cycle()
        
    def check_signal_strength(self):
        for instruction in self.instructions:
            #run instruction
            if len(instruction.split()) == 1: self.noop()
            else: self.addx(int(instruction.split()[1]))
        return self.total_signal_strength
    
    def make_screen(self):
        for instruction in self.instructions:
            #run instruction
            if len(instruction.split()) == 1: self.noop()
            else: self.addx(int(instruction.split()[1]))
        print(self)
    
    def __str__(self):
        for row in self.screen:
            printable_row = ''
            for character in row:
                printable_row += character
            print(printable_row)
        return ''


pt1_crt = CRT(instructions)
print(f"The sum of the signal strengths is {pt1_crt.check_signal_strength()}")

#the sprite is 3 pixels wide. X is middle of sprite
# 40 wide and 6 high. 
# draws the top row left-to-right, then the row below that, etc
# The left-most pixel is position 0, and the right-most pixel is position 39.
# draws a single pixel during each cycle
# If one of the sprite's three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.).

pt2_crt = CRT(instructions)
pt2_crt.make_screen()
