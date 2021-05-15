greetings = "Sup, This program is designed to let you know which Generation you ended up in Depending on your Birthdate"
choice = "Do you wanna know which Generation are you in (Y)eah or (N)ahh ?"
print(greetings)

choice = input(choice)
choice = choice.capitalize()
result = choice.startswith("N")

if result:
    quit("Whatever.")

else:
    print("Here we Go")


age = float(input("Tell us your BirthDate"))

if 2012 < age < 2020:
    print("you're from generation Alpha")

if 1997 < age < 2012:
    print("you're from generation Z")

if 1981 < age < 1997:
    print("you're from generation Y")
if 1965 < age < 1980:
    print("you're from generation X")
if 1946 < age < 1964:
    print("you're from generation Baby Boomers")
if 1928 < age < 1945:
    print("you're from generation Silent Generation")
if 1901 < age < 1927:
    print("you're from generation Greatest Generation")
if 1883 < age < 1900:
    print("you're from generation Lost Generation")
print(" Now you know, I hope you enjoyed it, take care")
