# Write your code here :-)
collon = input('Enter a letter of collon (a to h): ')
row = int(input('Enter a number of row (1 to 8): '))

letter = ('a','c','e','g')
if (collon in "aceg") == (row % 2 == 1):
        color = 'black'
else:
        color = 'white'
print (color)
