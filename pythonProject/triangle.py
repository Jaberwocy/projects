
nomimus = input("Enter a nominal: ")

money = {
    '1': "George Washington",
    '2': "Thomas Jefferson",
    '5': "Abraham Lincoln",
    '10': "Alexander Hamilton",
    '20': "Andrew Jackson",
    '50': "Ulysses Grant",
    '100': "Benjamin Franklin"
}
if nomimus not in money:
    print("Wrong nominal")
else:
    print("In ", nomimus, "dollars printed", money[nomimus])
