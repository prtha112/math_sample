# https://tuenongfree.xyz/%E0%B8%AA%E0%B8%A1%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%AA%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%A3%E0%B8%87/

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
