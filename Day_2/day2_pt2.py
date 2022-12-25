#  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

choice_to_number = { "A": 1, "B": 2, "C": 3 }
result_to_number = { "X": 0, "Y": 3, "Z": 6 }

def your_choice(oppontents_pick, result):
    # we lose
    if result == 0: 
        our_choice = oppontents_pick - 1
        if our_choice == 0: our_choice = 3
        return our_choice
    # we draw
    elif result == 3:
        return oppontents_pick
    # we win
    else:
        our_choice = oppontents_pick + 1
        if our_choice == 4: our_choice = 1
        return our_choice
        
        
def determine_score(oppontents_pick, result):
    result = result_to_number[result]
    your_pick = your_choice(choice_to_number[oppontents_pick], result)
    
    return result + your_pick
    

# split input into list
rounds = open("day2_input.txt","r").read().split("\n")

#get scores
scores = []
for choices in rounds:
    scores.append(determine_score(choices[0], choices[2]))

#add up scores
print("Your score is: %d" % sum(scores))
