# split input per rucksack
rucksacks = open("day3_input.txt","r").read().split("\n")

priority_of = {
    "a": 1, "A": 27,
    "b": 2, "B": 28,
    "c": 3, "C": 29,
    "d": 4, "D": 30,
    "e": 5, "E": 31,
    "f": 6, "F": 32,
    "g": 7, "G": 33,
    "h": 8, "H": 34,
    "i": 9, "I": 35,
    "j": 10, "J": 36,
    "k": 11, "K": 37,
    "l": 12, "L": 38,
    "m": 13, "M": 39,
    "n": 14, "N": 40,
    "o": 15, "O": 41,
    "p": 16, "P": 42,
    "q": 17, "Q": 43,
    "r": 18, "R": 44,
    "s": 19, "S": 45,
    "t": 20, "T": 46,
    "u": 21, "U": 47,
    "v": 22, "V": 48,
    "w": 23, "W": 49,
    "x": 24, "X": 50,
    "y": 25, "Y": 51,
    "z": 26, "Z": 52,
}

priorities = []

for i in range(0,len(rucksacks),3):
    first_rucksack = rucksacks[i]
    second_rucksack = rucksacks[i+1]
    third_rucksack = rucksacks[i+2]
    
    for supply in first_rucksack:
        if (supply in second_rucksack) and (supply in third_rucksack):
            priorities.append(priority_of[supply])
            break

print("The sum of priorities %d" % sum(priorities))
