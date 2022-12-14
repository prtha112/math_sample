number = [600,470,170,430,300] 

def variance(number):
    sum_number = 0
    for _number in number:
        sum_number = sum_number + _number
    mean_number = sum_number/len(number)
    
    sum_diff = []
    for _number in number:
        diff = (_number - mean_number)
        diff_pow2 = diff ** 2
        sum_diff.append(diff_pow2)
        
    sum_variance = sum(sum_diff)/len(sum_diff)
    return sum_variance
    
print(variance(number))
