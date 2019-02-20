import numpy as np

# numpy的随机数函数


# numpy的random子库：np.random.*，主要有np.random.rand()   np.random.randn()   np.random.randint()

# rand(d0,d1,d2,……，dn)  :  根据d0-dn创建随机数组，浮点数，范围是[0,1),均匀分布
a = np.random.rand(2, 3, 4)
print(a)
"""
[[[0.4506612  0.5296636  0.9747625  0.90105177]
  [0.25850117 0.90704491 0.87144252 0.00418912]
  [0.69423447 0.690204   0.4432447  0.37734196]]

 [[0.41056822 0.4220897  0.80819521 0.99022746]
  [0.61803924 0.93554027 0.3742707  0.94081985]
  [0.15283965 0.09844152 0.25726209 0.24488101]]]
"""

# randn(d0,d1,d2,……，dn)  :  根据d0-dn创建随机数组,标准正态分布
a = np.random.randn(2, 3, 4)
print(a)

# randint(low, high, shape) : 根据shape创建随机数数组，范围是[low, high)
a = np.random.randint(5, 10, (2, 3, 4))
print(a)
"""
[[[5 6 5 7]
  [7 5 9 5]
  [6 7 6 5]]

 [[8 6 7 5]
  [6 8 5 6]
  [8 8 7 9]]]
"""
# seed(s) : 随机数种子，s是给定的种子值
# np.random.seed(5)
# a = np.random.randint(5, 10, (2, 3, 4))
# print(a)
"""
[[[8 5 6 5]
  [9 8 5 5]
  [9 6 5 8]]

 [[9 8 6 9]
  [7 6 6 7]
  [6 6 6 7]]]
"""
# 如上图：当给定的种子值为4时，数组的值并不会改变

# shuffle(a): 根据数组a的每一纵列进行随机排列，数组a发生改变
a = np.random.randint(5, 10, (3, 4))
print(a)
"""
[[[6 8 7 8]
  [9 7 7 9]
  [5 6 6 8]]

 [[6 6 5 6]
  [5 7 5 5]
  [6 8 5 9]]]
"""
np.random.shuffle(a)
print(a)
"""
[[8 7 8 7]
 [5 6 5 8]
 [7 9 5 5]]
[[5 6 5 8]
 [8 7 8 7]
 [7 9 5 5]]
"""

# permutation(a) ：根据数组a的每一纵列进行随机排列，数组a不改变

a = np.random.randint(5, 10, (3, 4))
print(a)
"""
[[8 7 5 9]
 [5 9 8 6]
 [6 6 5 5]]
"""
b = np.random.permutation(a)
print(a)
"""
[[9 5 7 9]
 [5 9 5 7]
 [6 8 6 7]]
"""
print(b)
"""
[[5 9 5 7]
 [6 8 6 7]
 [9 5 7 9]]
"""

# choice(a, size, replace, p)：从一维数组a中以概率p抽取元素，形成size形状的新数组，replace表示是否可以重用元素，默认为True
a = np.arange(6)

print(np.random.choice(a, 2, replace=False, p=a / np.sum(a)))
# replace在一维数组中有效


"""
uniform(low, high, size)  : 产生具有均匀分布的数组,low起始值,high结束值,size形状

normal(loc,scale,size)   :  产生具有正态分布的数组,loc均值,scale标准差,size形状

poisson(lam,size)  :   产生具有泊松分布的数组,lam随机事件发生率,size形状

"""

# numpy的统计函数：
# np.sum(a, axis=None) ： 根据给定轴axis计算数组a相关元素之和,axis整数或元组。

a = np.arange(15).reshape((3, 5))
print(a)
"""
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
"""
print(np.sum(a, axis=0))
# [15 18 21 24 27]
print(np.sum(a, axis=1))
# [10 35 60]
"""
当axis=None时，np.sum(a)表示数组a的所有元素总和

当axis=0时，表示的是数组a各纵列元素之和

当axis=1时，表示的是数组a各横列元素之和

mean(a, axis=None) ：根据给定轴axis计算数组a相关元素的期望,axis整数或元组
"""

# mean 求取均值
print(1, np.mean(a))
print(np.mean(a, axis=0))

# average(a,axis=None,weights=None)：根据给定轴axis计算数组a相关元素的加权平均值
print(np.average(a, axis=0, weights=[2, 3, 4]))
# [ 6.11111111  7.11111111  8.11111111  9.11111111 10.11111111]
# 6.111111111111111是这样计算出来的: (0 * 2 + 5 * 3 + 4 * 10) / (2 + 3 + 4)

"""
std(a, axis=None) : 根据给定轴axis计算数组a相关元素的标准差

var(a, axis=None) :  根据给定轴axis计算数组a相关元素的方差

min(a)  max(a) :  计算数组a中元素的最小值、最大值

argmin(a)  argmax(a) :  计算数组a中元素最小值、最大值的降一维后下标

unravel_index(index, shape) :  根据shape将一维下标index转换成多维下标

ptp(a) :  计算数组a中元素最大值与最小值的差

median(a)  :   计算数组a中元素的中位数(中值)

"""

print("----------梯度函数------------")

"""
np.gradient(a)  ：计算数组a中元素的梯度,当a为多维时,返回每个维度梯度

梯度:连续值之间的变化率,即斜率

XY坐标轴连续三个X坐标对应的Y轴值:a, b, c,其中,b的梯度是: (c‐a)/2
"""

a = np.random.randint(0, 20, (5))
print(a)
# [ 5  5 13  6 10]
print(np.gradient(a))
# [ 0.   4.   0.5 -1.5  4. ]
#  0 : (5-5)/1
#  4. : (10-6)/1
#  0.5: (6-5)/2
#  4. : (13-5)/2


# 当a为多维数组时

a = np.arange(12).reshape(2,6)
print(a)
"""
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
"""
print(np.gradient(a))
"""
[array([[6., 6., 6., 6., 6., 6.],
       [6., 6., 6., 6., 6., 6.]]), array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])]
"""
# 上侧表示最外层维度(axis=0)的梯度,下侧表示第二层维度(axis=1)的梯度。