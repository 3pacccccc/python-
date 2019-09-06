# -*- coding: utf-8 -*-

import time

start_time = time.time()

# # 方法1(花费了844秒)
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
#                 print("a={0}, b={1}, c={2}".format(a, b, c))

# 方法2(花费了0.471秒)
for a in range(0, 1001):
    for b in range(0, 1001 - a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a={0}, b={1}, c={2}".format(a, b, c))

end_time = time.time()
print("spend {0} seconds".format(end_time - start_time))

