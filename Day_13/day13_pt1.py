# these are lists or lists of lists
test_input = [list(map(eval,duo.split("\n"))) for duo in open("day13_test_input.txt","r").read().split("\n\n")]
distress_signal = [list(map(eval,duo.split("\n"))) for duo in open("day13_input.txt","r").read().split("\n\n")]

# if left and right are integers, lower integer comes first
# if left and right are lists, go inside list. if left runs out of values before right, we're in order
# if one is a list and the other one isn't: convert the integer int into a list: [int], then compare the lists

def is_in_correct_order(left,right):
    #print("left",left,"right",right)
    #print("Types:")
    if type(left) is int and type(right) is int:
        #print("int int")
        if left < right: 
            #print("true");
            return True
        elif left > right: 
            #print("false");
            return False
        else: 
            #print("can't determine"); 
            return "who knows"
    #has to be rehandled:
    elif type(left) is list and type(right) is list:
        #print("list list")
        for i in range(len(left)):
            #print("list subindex",i)
            if i > len(right) - 1: #if right ran our of items before left
                #print("we ran out of right first")
                return False
            result = is_in_correct_order(left[i],right[i])
            if result == "who knows": continue
            elif result: return True
            else: return False
        if len(left) < len(right):
            #print("left is shorter")
            return True
        else: 
            #print("can't determine");
            return "who knows"
    #one of them is a list and the other one isn't 
    elif type(left) is list and type(right) is int:
        #print("list int")
        return is_in_correct_order(left,[right])
    elif type(left) is int and type(right) is list:
        #print("int list")
        return is_in_correct_order([left],right)
    #else:
    #    print("what")
    
def get_sum_of_indices(distress_signal):
    index_sum = 0
    for i in range(len(distress_signal)):
        #print("################# pair #", i+1, "#################")
        left = distress_signal[i][0]
        right = distress_signal[i][1]
        if is_in_correct_order(left,right):
            #print("adding index",i+1)
            index_sum += (i+1)
    return index_sum

print('### pt1 ###')
print("Test:")
print(f'The sum of indices in correct order is: {get_sum_of_indices(test_input)}')
print("Real:")
print(f'The sum of indices in correct order is: {get_sum_of_indices(distress_signal)}')

