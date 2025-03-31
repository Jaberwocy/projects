# Write your code here :-)
month = input("Enter a month of the year: ")

month31 = ('january', 'march', 'may', 'july', 'augest', 'october','december')

if month == 'february':
    print('In February may be 28 or 29 days')
elif month in month31:
    print('In', month, '31 days')
else:
    print('In', month, '30 days')


