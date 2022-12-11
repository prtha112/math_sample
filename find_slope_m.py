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

c = find_y_intercept(2,5)
m = find_slope(2, 5, 4, 9)

print(find_slope_m(m, c));
