# 数学函数
# ```
# 本次学习内容为数学函数，顾名思义，就是常见的数学上的操作，最基础的有：加减乘除等
# 运算符为 元素级，只用于位置相同的元素之间，所得到的运算结果组成一个
# 新的数组
# ```
## 基础的数学操作
# - 加法
#   ```
#   numpy.add(x1, x2, *args, **kwargs)
#   ```
# - 减法
#   ```
#   numpy.subtract(x1, x2, *args, **kwargs)
#   ```
# - 乘法
#   ```
#   numpy.multiply(x1, x2, *args, **kwargs)
#   ```
# - 除法
#   ```
#   numpy.divide(x1, x2, *args, **kwargs)
#   ```
# - 除法，只保留整数
#   ```
#   numpy.floor_divide(x1, x2, *args, **kwargs)
#   ```
# - N次方
#   ```
#   numpy.power(x1, x2, *args, **kwargs)
#   ```
import numpy as np 

x = np.arange(25,37).reshape([3,4])
print(x)

# y = x + 1
print(np.add(x,1))
print(np.subtract(x, 1))
print(np.multiply(x, 2))
print(np.divide(x, 2))
print(np.floor_divide(x, 3))
print(np.power(x, 2))


y = np.arange(1,13).reshape([3,4])


print(np.add(x, y))
print(np.subtract(x, y))
print(np.multiply(x, y))

# - 平方根
#   ```
#   numpy.sqrt(x1, x2, *args, **kwargs)
#   ```
print(np.sqrt(x))
# - 平方
#   ```
#   numpy.square(x1, x2, *args, **kwargs)
#   ```

print(np.square(x)) # == print(np.power(x,2))

print(np.power(y, 3))

# 三角函数
#   ```
#   几何图形三角函数，常用的：求正弦值，余弦值
#   ```

## 三角函数操作
# - 正弦值
#   ```
#   numpy.sin(x1, x2, *args, **kwargs)
#   ```
#   ```
#   numpy.cos(x1, x2, *args, **kwargs)
#   ```
#   ```
#   numpy.tan(x1, x2, *args, **kwargs)
#   ```
#   ```
#   numpy.arcsin(x1, x2, *args, **kwargs)
#   ```
#   ```
#   numpy.arccos(x1, x2, *args, **kwargs)
#   ```
#   ```
#   numpy.arctan(x1, x2, *args, **kwargs)
#   ```
# 要点 2
# 通用函数（universal function）通常叫作ufunc，它对数组中的各个元素逐一进行操作。这表明，通用函数分别处理输入数组的每个元素，生成
# 的结果组成一个新的输出数组。输出数组的大小跟输入数组相同
# 很多数学运算符合通用函数的定义，例如，计算平方根的sqrt() 函数、用来取对数的log() 函数和求正弦值的sin() 函数

l  = np.linspace(start=0, stop=np.pi / 2, num=10)

print(l)


# 要点3 
# 通过不同的 axis ，numpy 会沿着不同的方向进行操作：如果不设置，那么对所有的元素操作；如果axis=0 ，则沿着纵轴进行操
# 作； axis=1 ，则沿着横轴进行操作。但这只是简单的二位数组，如果是多维的呢？可以总结为一句话：设axis=i ，则 numpy 沿着第i 个
# 下标变化的方向进行操作。

# 要点 4
# 聚合函数 是指对一组值（比如一个数组）进行操作，返回一个单一值作为结果的函数。因而，求数组所有元素之和的函数就是聚合函
# 数。ndarray 类实现了多个这样的函数。

# 要点 5 
# 上限 基本上是 +1
# 下限 是只取整数

# numpy.clip
# 裁剪 等于把数组里小于裁剪下限的值换成下限值，大于上限的值换成上限值
