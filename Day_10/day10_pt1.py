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


cycle = 1
X = 1
total_signal_strength = 0

# addX V takes 2 cycles, after: X += V
# noop = do nothing for one cycle

def check_cycle():
    if cycle%40 == 20: #if we're at one of the special cycles
        global total_signal_strength
        total_signal_strength += cycle*X

def addx(V):
    global cycle; global X
    cycle+=1
    check_cycle()
    cycle+=1; X+=V
    check_cycle()

def noop():
    global cycle
    cycle+=1
    check_cycle()

fn = {
    'addx': addx,
    'noop': noop,
}


def check_signal_strength(instructions):
    for instruction in instructions:
        #run instruction
        if len(instruction.split()) == 1: fn[instruction.split()[0]]()
        else: fn[instruction.split()[0]](int(instruction.split()[1]))
    return total_signal_strength

print(f"The sum of the signal strengths is {check_signal_strength(instructions)}")
