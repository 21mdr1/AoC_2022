# split input per elf
calories = open("day1_input.txt","r").read().split("\n\n")

#sum out each elf
for elf in range(len(calories)):
    calories[elf] = sum(map(int,calories[elf].split("\n")))

#get the max of the elves
print("The max number of calories are %d" % max(calories))
