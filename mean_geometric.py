number = [2,14,8] 

def geometric_mean(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product ** (1 / len(numbers))
    
print(geometric_mean(number))
