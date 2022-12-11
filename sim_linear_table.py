def find_y_intercept(x, y):
  # c = y - 2x
  c = y - (2 * x)
  return c;

def find_slope(x1, y1, x2, y2):
  # M = (y2-y1)/(x2-x1)
  m = (y2-y1)/(x2-x1)
  return m

def find_slope_m(m, c):
  # Y = mx + c
  y = "y = {0}x + {1}".format(m, c);
  return y

def get_digit(number, n):
  return number // 10**n % 10

def sim_linear_table(x, y):
  len_x = len(x)
  len_y = len(y)
  if len_x != len_y:
    raise ValueError("Length not valid.")
  avg_x = sum(x)/len_x
  avg_y = sum(y)/len_y

  sum_d = 0
  sum_c_e = 0
  b1 = 0
  b0 = 0
  
  num = 0
  res_x = []
  for _x in x:
    res = {}
    
    c = (_x - avg_x)
    d = c ** 2
    e = y[num] - avg_y
    c_e = c * e
    
    res["c"] = "%.2f" % c
    res["d"] = "%.2f" % d
    res["e"] = "%.2f" % e
    res["c_e"] = "%.2f" % c_e

    sum_d = sum_d + d
    sum_c_e = sum_c_e + c_e
    
    res_x.append(res)
    num = num + 1

  print(res_x)
  b1 = sum_c_e / sum_d
  b0 = avg_y - (b1 * avg_x)
  b = [b0, b1]
  return b

x = [2, 4, 6, 8, 10, 12]
y = [6, 10, 11, 14, 22, 25]

print(sim_linear_table(x, y))
