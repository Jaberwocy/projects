# Write your code here :-)
month = input ("Enter a month: ")
day = int( input("Enter a date: "))

year = {
'winter':('January', 'February',"March" ),
'spring':('April', 'May', 'June'),
'summer':('July','Augest', 'September'),
'autumn':('October', 'November','December')
}

season = ''
if 21>day:
    for key, months in year.items():
        if month in months:
            season = key
            break
        else:
            if month == "March":
                season = 'spring'
            elif month == "June":
                season = 'spring'
            elif month == "September":
                season = 'autumn'
            elif month == "December":
                season = 'winter'

print (season)





