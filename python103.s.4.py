# Python103, small, exercise 4
#Print NxN square

#defining user input var 
user_num = input('Enter a number for square size: ')

#turning user_num into an integer
int_num = int(user_num)

# defining var to hold '*' string
aster = '*'

#creating new aster based on how big user wants square to be
aster_size = aster * int_num

# defining counter
count = 0

# printing aster based on # of iterations specified by user

while count < int_num:
    print(aster_size)
    count += 1