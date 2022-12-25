# split input per elf
calories = open("day1_input.txt","r").read().split("\n\n")

#sum out each elf
for elf in range(len(calories)):
    calories[elf] = sum(map(int,calories[elf].split("\n")))

#sum three max elves
calories.sort(reverse=True)
print("The three max calories summed are %d" % (calories[0] + calories[1] + calories[2]))
