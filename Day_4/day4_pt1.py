import re

# split by elf pairs
pairs = [tuple(map(int,re.split(",|-",pair))) for pair in open("day4_input.txt","r").read().split("\n")]

problem_pairs=0
for pair in pairs:
    first_elf_start = pair[0]
    first_elf_end = pair[1]
    second_elf_start = pair[2]
    second_elf_end = pair[3]
    if (first_elf_start >= second_elf_start and first_elf_end <= second_elf_end) or (first_elf_start <= second_elf_start and first_elf_end >= second_elf_end):
        problem_pairs+=1

print("Pairs with problems: %d" % problem_pairs)
