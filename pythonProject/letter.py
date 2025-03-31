# Write your code here :-)

litera = input("Enter a litera of latin alfabet: ")

glas = ("a", 'e', 'i', 'o', 'u')


if litera in glas:
    print ("You enter a vowel letter")
elif litera == 'y':
    print ("You entered y. This letter can be either a vowel or a consonant.")
else:
    print("You have entered a consonant letter")
