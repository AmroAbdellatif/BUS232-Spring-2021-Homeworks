def reverse(s):
    str = ""
    for i in s:
        if i != ' ':
            str = i + str
    return str.lower()


string = input("lets play a reverse game Just say anything \n")
reversedString = reverse(string)
print('\n' + reversedString)
