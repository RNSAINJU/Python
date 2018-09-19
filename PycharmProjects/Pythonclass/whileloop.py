# count =0
# while True:
#     count += 1
#     if count >= 10:
#             break
#     print(count)

#!/usr/bin/env python3.7
# import time
# count = 10
# while True:
#     print(count)
#     if count <= 0:
#         print('Happy Birthday')
#         break
#     time.sleep(1)
#     count -= 1


a , b=0,1

while True:
    a ,b = b, a+b

    if a>=50:
        break
    print(a)
