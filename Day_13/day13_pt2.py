from functools import cmp_to_key
# these are lists or lists of lists
test_input_pt1 = [list(map(eval,duo.split("\n"))) for duo in open("day13_test_input.txt","r").read().split("\n\n")]
distress_signal_pt1 = [list(map(eval,duo.split("\n"))) for duo in open("day13_input.txt","r").read().split("\n\n")]


def get_list_of_lists(input_file):
    lists = []
    for line in open(input_file,"r").read().split("\n"):
        if not line == "":
            lists.append(eval(line))
    return lists

test_input_pt2 = get_list_of_lists("day13_test_input.txt")
distress_signal_pt2 = get_list_of_lists("day13_input.txt")

# if left and right are integers, lower integer comes first
# if left and right are lists, go inside list. if left runs out of values before right, we're in order
# if one is a list and the other one isn't: convert the integer int into a list: [int], then compare the lists


"""def is_in_correct_order(left,right):
    print("left",left,"right",right)
    print("  Types:")
    if type(left) is int and type(right) is int:
        print("    int int")
        if left < right: 
            print("true");
            return True
        elif left > right: 
            print("false");
            return False
        else: 
            print("      can't determine"); 
            return "who knows"
    elif type(left) is list and type(right) is list:
        print("    list list")
        if len(left) == 0 or len(right) == 0: 
            print("      one of these lists is empty,", len(left) < len(right))
            return len(left) < len(right)
        for i in range(len(left)):
            print("      list subindex",i)
            if i > len(right) - 1: #if right ran our of items before left
                print("      we ran out of right first, false")
                return False
            result = is_in_correct_order(left[i],right[i])
            if result == "who knows": continue
            elif result: return True
            else: return False
        if len(left) < len(right):
            print("      left is shorter, true")
            return True
        else: 
            print("      can't determine");
            return "who knows"
    #one of them is a list and the other one isn't 
    elif type(left) is list and type(right) is int:
        print("    list int")
        return is_in_correct_order(left,[right])
    elif type(left) is int and type(right) is list:
        print("    int list")
        return is_in_correct_order([left],right)
    else:
        print("################# what #################")"""

def is_in_correct_order(left,right):
    #print("left",left,"right",right)
    #print("  Types:")
    if type(left) is int and type(right) is int:
        #print("    int int")
        if left < right: 
            #print("true");
            return 1
        elif left > right: 
            #print("false");
            return -1
        else: 
            #print("      can't determine"); 
            return "who knows"
    elif type(left) is list and type(right) is list:
        #print("    list list")
        if len(left) == 0 or len(right) == 0: 
            #print("      one of these lists is empty,", len(left) < len(right))
            if len(left) < len(right): return 1
            else: return -1
        for i in range(len(left)):
            #print("      list subindex",i)
            if i > len(right) - 1: #if right ran our of items before left
                #print("      we ran out of right first, false")
                return -1
            result = is_in_correct_order(left[i],right[i])
            if result == "who knows": continue
            elif result == 1: return 1
            else: return -1
        if len(left) < len(right):
            #print("      left is shorter, true")
            return True
        else: 
            #print("      can't determine");
            return "who knows"
    #one of them is a list and the other one isn't 
    elif type(left) is list and type(right) is int:
        #print("    list int")
        return is_in_correct_order(left,[right])
    elif type(left) is int and type(right) is list:
        #print("    int list")
        return is_in_correct_order([left],right)
    #else:
        #print("################# what #################")


def get_sum_of_indices(distress_signal):
    index_sum = 0
    for i in range(len(distress_signal)):
        #print("################# pair #", i+1, "#################")
        left = distress_signal[i][0]
        right = distress_signal[i][1]
        if is_in_correct_order(left,right) == 1:
            #print("adding index",i+1)
            index_sum += (i+1)
    return index_sum


def get_delimiter_indices(distress_signal):
    distress_signal += [[[2]],[[6]]]
    sorted_signal = sorted(distress_signal,key=cmp_to_key(is_in_correct_order),reverse=True)
    return (sorted_signal.index([[2]]) + 1) * (sorted_signal.index([[6]]) + 1)


print('### pt1 ###')
print("Test:")
print(f'The sum of indices in correct order is: {get_sum_of_indices(test_input_pt1)}')
print("Real:")
print(f'The sum of indices in correct order is: {get_sum_of_indices(distress_signal_pt1)}')

print('### pt2 ###')
print(f'The product of delimiter indices is: {get_delimiter_indices(test_input_pt2)}')
print("Real:")
print(f'The product of delimiter indices is: {get_delimiter_indices(distress_signal_pt2)}')

