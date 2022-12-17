from statistics import mean 

number = [2000,5000,2150,4130,2564] 

def variance(number, population):
  if population == True:
      pop = 1
  else:
      pop = 0
    
  mean_number = sum(number)/len(number)
  sum_diff = []
    
  for _number in number:
    diff = (_number - mean_number)
    diff_pow2 = diff ** 2
    sum_diff.append(diff_pow2)
        
  sum_variance = sum(sum_diff)/(len(sum_diff) - pop)
  return sum_variance
    
def standardDeviation(number):
  # square root
  return number**(1/2)

def standard_scaler(number, avg, std):
  num_list = []
  for _n in number:
    num_list.append((_n - avg) / std)
  return num_list

u = mean(number)
variance = variance(number, False)
std = standardDeviation(variance)
z = standard_scaler(number, u, std)

print(z)
