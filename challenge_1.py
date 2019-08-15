# TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the coordinate specified by the user

print()
print('Here is my grid!')
print()

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

print_counter = 0
for list in five_by_five_grid:
    print (list)
    print_counter += 1

print()
print('Do you like my grid?')
print()
print('No...?')
print()

change_row = int(input('Then tell me what row coordinate of what you would like to change? '))
print()
change_col = int(input('And what column coordinate of what you would like to change? '))

#create row_six
row_six = []

second_count = 0
verti = 0
horiz = 0
for col in range(len(five_by_five_grid)):
    for row in five_by_five_grid:
        if five_by_five_grid[verti][horiz] == 'X':
            second_count += 1
        verti += 1
    if second_count % 2 == 0:
        row_six.append('0')
    else:
        row_six.append('X')
    second_count = 0
    verti = 0
    horiz += 1

five_by_five_grid.append(row_six)

# #add column 6
for list in five_by_five_grid:
    count = 0
    for item in list:
        if item == 'X':
            count += 1
    if count % 2 == 0:
        list.append('0')
    else:
        list.append('X')



if five_by_five_grid[change_row][change_col] == 'X':
    five_by_five_grid[change_row][change_col] = '0'
else:
    five_by_five_grid[change_row][change_col] = 'X'

#print grid
print()
print_counter = 0
for list in five_by_five_grid:
    print (list)
    print_counter += 1

print()
print('What you have done to my grid!?')

# row test

rows = len(five_by_five_grid)
columns = len(five_by_five_grid)
xes = 0
xes_two = 0

for a in range(rows):
    for b in range (columns):
        if five_by_five_grid [a][b] == 'X':
            xes += 1
    if xes % 2 == 1:
        break
    else:
        xes = 0
        

print('You changed row', a)

# column test

for c in range(columns):
    for d in range(rows):
        if five_by_five_grid [d][c] == 'X':
            xes_two += 1
    if xes_two % 2 == 1:
        break
    else:
        xes_two = 0

print ('You changed column', c)