forest =[list(map(int,[*row])) for row in open("day8_input.txt","r").read().split("\n")]


def is_visible(tree,direction):
    # returns True if visible and False if not
    # the case where tree is at the edge will be handled outside this function
    y,x = map(int, tree.split(","))
    our_tree_height = forest[y][x]
    # lets get the trivial case out of the way
    if our_tree_height == 0:
        return False
    # now lets look per direction
    if direction == "up":
        #y decreases
        for coordinate in range(y):
            other_tree_height = forest[coordinate][x]
            if  other_tree_height >= our_tree_height:
                return False
        return True
    elif direction == "down":
        #y increases
        for coordinate in range(y+1,len(forest)):
            other_tree_height = forest[coordinate][x]
            if  other_tree_height >= our_tree_height:
                return False
        return True
    elif direction == "right":
        #x increses
        for coordinate in range(x+1,len(forest[y])):
            other_tree_height = forest[y][coordinate]
            if  other_tree_height >= our_tree_height:
                return False
        return True
    elif direction == "left":
        #x decreases
        for coordinate in range(x):
            other_tree_height = forest[y][coordinate]
            if  other_tree_height >= our_tree_height:
                return False
        return True
    else: return NotImplemented

#start with the outside trees:
visible_trees = len(forest)*2 + len(forest[0])*2 - 4
for y in range(1,len(forest)-1):
    for x in range(1,len(forest[y])-1):
        tree = str(x) + "," + str(y)
        if is_visible(tree,"up") or is_visible(tree,"down") or is_visible(tree,"right") or is_visible(tree,"left"):
            visible_trees+=1

print(f"The number of visible trees is {visible_trees}")

