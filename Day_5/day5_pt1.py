# get input
input_file = open("day5_input.txt","r").read().split("\n\n")

initial_arrangement = input_file[0].split("\n")
moves = input_file[1].split("\n")

# get initial state
arrangement = []
for i in initial_arrangement[-1].split():
    arrangement.append([])

for row in list(reversed(initial_arrangement))[1:]:
    crate_size = 4
    counter=-1
    for i in range(0,len(row),crate_size):
        counter+=1
        crate = row[i:i+crate_size]
        if crate in "    ":
            continue
        arrangement[counter].append(crate[1])

#make the moves
for move in moves:
    #get move
    move_list = move.split(" ")
    
    number_of_crates = int(move_list[1])
    start_column = int(move_list[3])-1
    end_column = int(move_list[5])-1 
    
    #make move
    for i in range(number_of_crates):
        arrangement[end_column].append(arrangement[start_column].pop(-1))

#format answer
answer = ""
for column in arrangement:
    answer += column[-1]

print("The top crates are: %s" % answer)
