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

def predict(b0, b1, x):
  y_predict = b0 + (b1 * x)
  return y_predict

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

  b1 = sum_c_e / sum_d
  b0 = avg_y - (b1 * avg_x)
  b = [b0, b1]
  return b

def sim_linear_score(x, y, b0, b1):
  len_x = len(x)
  len_y = len(y)
  if len_x != len_y:
    raise ValueError("Length not valid.")
  avg_x = sum(x)/len_x
  avg_y = sum(y)/len_y

  sum_rss = 0
  sum_tss = 0
  
  num = 0
  res_x = []
  for _x in x:
    res = {}
    y_predict = predict(b0, b1, _x)
    rss = (y[num] - y_predict) ** 2
    tss = (y[num] - avg_y) ** 2

    sum_rss = sum_rss + rss
    sum_tss = sum_tss + tss
    num = num + 1
  return 1 - sum_rss / sum_tss, sum_rss

def mse(rss, y):
  return (rss/y)

def rmse(rss, y):
  return (rss/y)**(1/2)

x = [2, 4, 6, 8, 10, 12]
y = [6, 10, 11, 14, 22, 25]

b = sim_linear_table(x, y)
predicts = predict(b[0], b[1], 10)
score = sim_linear_score(x, y, b[0], b[1])
print(predicts)
print(score)
print(mse(score[1], y[0]))
print(rmse(score[1], y[0]))
# Predict : 20.409523809523808
# R-Squared Score : 0.9453843453843453
# MSE : 2.4698412698412713
# RMSE : 1.5715728649481293
