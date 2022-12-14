w = [2,14,8,32] # w for the number of weeks (the weight)
x = [1,2,5,7] # x for lunches (the value we want the mean of)

def mean_weigh(x, w):
    num = 0
    w_sum = 0
    wx_sum = 0
    for _x in x:
        w_tmp = w[num]
        wx_tmp = _x * w_tmp
        w_sum = w_sum + w_tmp
        wx_sum = wx_sum + wx_tmp
        num = num + 1
    return wx_sum/w_sum
        
print(mean_weigh(x, w))
