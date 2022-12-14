number = [600,470,170,430,300] 

def variance(number):
    mean_number = sum(number)/len(number)
    
    sum_diff = []
    for _number in number:
        diff = (_number - mean_number)
        diff_pow2 = diff ** 2
        sum_diff.append(diff_pow2)
        
    sum_variance = sum(sum_diff)/len(sum_diff)
    return sum_variance
    
def standardDeviation(number):
    # square root
    return number**(1/2)
    
print(variance(number))
print(standardDeviation(variance(number)))