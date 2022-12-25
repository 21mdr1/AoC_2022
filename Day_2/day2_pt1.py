# A = Rock = 1; B = Paper = 2; C = scissors = 3; this way scissors > paper > rock
# X = Rock = 1; Y = Paper = 2; Z = scissors = 3; this way scissors > paper > rock
# this also follows choice scores
choice_to_number = { "A": 1, "B": 2, "C": 3, "X":1, "Y": 2, "Z": 3 }

def determine_score(oppontents_pick, your_pick):
    # outcome scores
    win = 6; draw = 3; lose = 0
    
    # if choices are equal, we draw
    if choice_to_number[your_pick] == choice_to_number[oppontents_pick]:
        return choice_to_number[your_pick] + draw
    elif ( choice_to_number[your_pick] % 3 ) == ( (choice_to_number[oppontents_pick] + 1) % 3 ):
        return choice_to_number[your_pick] + win
    else:
        return choice_to_number[your_pick] + lose

# split input into list
rounds = open("day2_input.txt","r").read().split("\n")

#get scores
scores = []
for choices in rounds:
    scores.append(determine_score(choices[0], choices[2]))

#add up scores
print("Your score is: %d" % sum(scores))
