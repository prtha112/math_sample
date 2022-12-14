# Credit openai chatcgt
def quartiles(numbers):
    numbers.sort()
    n = len(numbers)

    if n % 2 == 0:
        Q1 = (numbers[n//4] + numbers[n//4 - 1]) / 2
        Q2 = (numbers[n//2] + numbers[n//2 - 1]) / 2
        Q3 = (numbers[3*n//4] + numbers[3*n//4 - 1]) / 2
    else:
        Q1 = numbers[n//4]
        Q2 = numbers[n//2]
        Q3 = numbers[3*n//4]

    return Q1, Q2, Q3
    
print(quartiles([3, 7, 8, 5, 12, 14, 21, 13, 18]))
