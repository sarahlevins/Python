# parity. how a computer detects errors in messages and compensates and fixed
## TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the
# coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]# output the grid with the flipped card
#add row 6
for list in five_by_five_grid:
    count = 0
    for item in list:
        if item =='X':
            count = count +1
    if count % 2 == 0:
        list.append('0')
    else:
        list.append('X')
#add column 6
for list in five_by_five_grid:
    x_count = 0
    for item in list:
        if item =='X':
            count += 1
        if count % 2 == 0:
            list.append('0')
        else:
            list.append('X')
# five_by_five_grid.append(five_by_five_grid[4])​
​#output the grid to the user
counter = 0
for list in five_by_five_grid:
    print (list)
    counter = counter +1
# ask the user for the coordinate of the card to flip
# e.g. input could be: (0,2)