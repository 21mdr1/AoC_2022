

# Falling rocks:
#              #          #       #
#  ####  -->  ###  -->    #  -->  #  -->  ##
#              #        ###       #       ##
#                                 #



# seven units wide
# #.......#
# #########


def move(dir):
    if dir == '>': x += 1
    elif dir == '<': x -= 1
    return x
