numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]


def transaction():
    for i, n in enumerate(numbers):

        length = len(numbers)
        if length == i + 1:
            break
        else:
            n1 = numbers[i]
            n2 = numbers[i + 1]
            result = n1 * n2
            text = 'Fake prime in position {3} is {2}.It is generated using {0} and {1}'.format(n1, n2, result, i + 1)
            print(text)


transaction()
