import numpy as np

# 对一维数组的切片

origin = np.arange(1,100)
print(origin)
print(origin[0:2])
print(origin[:12:4])
print(origin[:12:])
print(origin[5:])
print(origin[::-1]) #倒序

# 二维数组切片
origin = np.random.random((3,4))
print(origin)
print(origin[-2:,:2])
print(origin[::-2,::-1]) 