# TASK 1
# given a 5x5 grid, add the last column and row, then flip the card at the coordinate specified by the user

five_by_five_grid = [
    ['X','0','X','X','X'],
    ['X','X','0','0','0'],
    ['X','0','X','0','X'],
    ['0','X','X','X','X'],
    ['X','0','0','X','X'],
]

# #add column 6
# for list in five_by_five_grid:
#     count = 0
#     for item in list:
#         if item == 'X':
#             count += 1
#     if count % 2 == 0:
#         list.append('0')
#     else:
#         list.append('X')

#create row_six
row_six = []

second_count = 0
verti = 0
horiz = 0
for col in range(len(five_by_five_grid)):
    for row in five_by_five_grid:
        print (five_by_five_grid[verti][horiz])
        verti += 1
    verti = 0
    horiz += 1




#     if five_by_five_grid[verti][horiz] == 'X':
#         second_count += 1
#         verti += 1
# print(second_count)
# if second_count % 2 == 0:
#     row_six.append('0')
# else:
#     row_six.append('X')

# print(row_six)




#find out if number of X in row_six is odd. 
#if odd, append row_six with X
#if even, append row-six with 0

# counter = 0
# for list in five_by_five_grid:
#     print (list)
#     counter = counter +1