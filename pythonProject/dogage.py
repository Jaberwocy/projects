# Write your code here :-)

human_age = int(input("Enter human age: "))
dog_age=0
if human_age<0:
    print("Incorrect age. Please enter a positive number")
elif human_age <=21:
    dog_age = human_age/10.5
elif human_age>21:
    dog_age = 2+((human_age-21)//4)
print ("Your dog age is {:4.1f} ".format(dog_age), "years")


