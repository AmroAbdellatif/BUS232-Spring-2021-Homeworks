def printingShareHolder(Shares):
    l = len(sharesList)
    needed = sharesList[0]

    count = 1
    while count != l:
        if needed > Shares / 2:
            print('You need the support of top', count, 'shareholders for this number of votes')
            count = l
        else:
            count = count + 1
            needed = needed + sharesList[count]


inp = 1
shares = 0
sharesList = []

while inp != int(0):
    inp = int(input("Please enter the number of shares: "))
    shares = shares + int(inp)
    if inp < 0:
        print("Invalid input!")
    elif inp > 0:
        sharesList.append(inp)
print(sharesList)

print('the total', shares, 'shares represented here.')
print('Shares that are needed for majority vote is ', int(shares / 2), '.')

sharesList.sort()
sharesList.reverse()

printingShareHolder(shares)
