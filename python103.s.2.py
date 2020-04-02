# Python-103, small, exercise #2
#count to 10 and print numbers BUT prompt user for the number to start and end on

# defining start, turing into integer & printing
start = input('Enter a number between 1-9 to start counting: ')
ct_start = int(start)
print(f'Start counting at: {start}')

# defining end, turning into integer & printing
end = input('Enter a number between 2-10 to stop counting: ')
int_end = int(end)
print(f'Stop counting at: {end}')

count = ct_start

while count <= int_end:
    print(count)
    count += 1

    


