import numpy as np
import time

start = time.time()

print(np.sum(np.arange(1500000)))

end = time.time()

print(end - start)

# 1124999250000
# 0.004181623458862305
