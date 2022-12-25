forest =[list(map(int,[*row])) for row in open("day8_input.txt","r").read().split("\n")]

def visible_trees(tree,direction):
    # returns True if visible and False if not
    # the case where tree is at the edge will be handled outside this function
    x,y = map(int, tree.split(","))
    our_tree_height = forest[y][x]
    visible_trees = 0
    # lets get the trivial case out of the way
    if our_tree_height == 0:
        return 1
    # now lets look per direction
    if direction == "up":
        #y decreases
        for coordinate in reversed(range(y)):
            other_tree_height = forest[coordinate][x]
            visible_trees +=1 #if we made it here, we can see this tree
            if  other_tree_height >= our_tree_height:
                return visible_trees
        return visible_trees
    elif direction == "down":
        #y increases
        for coordinate in range(y+1,len(forest)):
            other_tree_height = forest[coordinate][x]
            visible_trees +=1
            if  other_tree_height >= our_tree_height:
                return visible_trees
        return visible_trees
    elif direction == "right":
        #x increses
        for coordinate in range(x+1,len(forest[y])):
            other_tree_height = forest[y][coordinate]
            visible_trees +=1
            if  other_tree_height >= our_tree_height:
                return visible_trees
        return visible_trees
    elif direction == "left":
        #x decreases
        for coordinate in reversed(range(x)):
            other_tree_height = forest[y][coordinate]
            visible_trees +=1
            if other_tree_height >= our_tree_height:
                return visible_trees
        return visible_trees
    else: return NotImplemented

highest_visibility_score = 0
for y in range(1,len(forest)-1):
    for x in range(1,len(forest[y])-1):
        tree = str(x) + "," + str(y)
        up = visible_trees(tree,"up")
        down = visible_trees(tree,"down")
        right = visible_trees(tree,"right")
        left = visible_trees(tree,"left")
        visibility_score = up*down*right*left
        if visibility_score > highest_visibility_score:
            highest_visibility_score = visibility_score

print(f"The highest visibility score is {highest_visibility_score}")

