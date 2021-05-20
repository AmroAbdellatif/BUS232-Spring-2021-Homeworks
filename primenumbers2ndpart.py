numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


def CheckPrimeNumber(number):
    if int(number) in numbers:
        return "Yup this Number is definitely a Prime"
    else:
        return 'Nope sorry this Number is not a Prime'


def primeNumberList():
    return numbers


def transactionJustResult():
    result = []
    for i, n in enumerate(numbers):
        length = len(numbers)
        if length == i + 1:
            print(result)
            break
        else:
            n1 = numbers[i]
            n2 = numbers[i + 1]
            result.append(n1 * n2)


checkNumber = input(" Number in mind : ")
print(CheckPrimeNumber(checkNumber))
print('Here is the Prime Numbers list : ')
print(primeNumberList())
print('the Result of the Fake Prime Numbers : ')
transactionJustResult()
