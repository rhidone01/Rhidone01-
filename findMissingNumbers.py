def findMissingNumbers(n):
    numbers = set(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
