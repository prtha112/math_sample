label = ['apple', 'banana', 'orange', 'orange']

def fit_transform(label):
  l = list(set(label))

  number = 0
  lab = {}
  for _l in l:
    lab[_l] = number
    number = number + 1
  return lab

def transform(label, label_map):
  arr = []
  for _l in label:
    arr.append(label_map[_l])
  return arr
  
label_map = fit_transform(label)
label_transform = transform(label, label_map)
print(label_transform)
