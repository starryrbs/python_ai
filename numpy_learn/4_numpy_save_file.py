import numpy as np

# 数据的CSV文件保存
"""
np.savetxt(frame, array, fmt='%.18e', delimiter=None)
frame:文件、字符串或产生器，可以是.gz或.bz2的压缩文件

array:存入文件的数组

fmt:写入文件的格式，例如：%d    %.2d     %.18e

delimiter : 分隔字符串，默认是任何空格
"""

a = np.arange(24).reshape((3, 8))

np.savetxt('a.csv', a, fmt='%d', delimiter=',')

# ‘a.csv’表示保存后的文件名是a.csv,a是要保存的数组,fmt=‘%d’是元素以整数类型保存，delimiter=','表示元素间以','分隔

# b = np.arange(24).reshape((2, 3, 4))
# np.savetxt('b.csv', b, fmt='%.2f', delimiter='^')
# csv文件不支持保存2维以上数据
# 否则会报错 ValueError: Expected 1D or 2D array, got 3D array instead


# 数据的csv文件读取

d = np.loadtxt('a.csv', delimiter=',')
print(d)

# 多维数组的保存
# a.tofile(frame, sep='', format='%s')
"""
frame  :  文件、字符串

sep :  数据分割字符串,如果是空串,写入文件为二进制

format  :  写入数据的格式


"""
a = np.arange(24).reshape((2, 3, 4))
a.tofile('a.dat', sep=',', format='%d')

# 注意：如果sep='',即数据分隔字符串是空串，写入的文件为二进制。
# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23
# 多维数组保存时,会转化为1维
# ubuntu读取二进制文件
# 1. sudo apt-get install libdata-hexdumper-perl
# 2. hexdump your_binary_file

# 多维数组的读取
# np.fromfile(frame, dtype=np.float, count=-1, sep='')
"""
frame  :  文件、字符串

dtype :  读取的数据类型

count  :  读入元素个数,‐1表示读入整个文件

sep :  数据分割字符串,如果是空串,写入文件为二进制
"""

c = np.fromfile('a.dat', dtype=np.int, sep=',').reshape((2, 3, 4))
print(c)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""

# numpy的便捷文件存取

# np.save(fname, array) 或 np.savez(fname, array)
"""
fname :  文件名,以.npy为扩展名,压缩扩展名为.npz

rray  :  数组变量
"""

# 读取
# np.load(fname)
# fname:  文件名,以.npy为扩展名,压缩扩展名为.npz

a = np.arange(24).reshape((2, 3, 4))
np.save('a.npy', a)

b = np.load('a.npy')
print(b)
"""
[[[ 0  1  2  3]
  [ 4  5  6  7]
  [ 8  9 10 11]]

 [[12 13 14 15]
  [16 17 18 19]
  [20 21 22 23]]]
"""

# 总结：
# numpy库提供的数据存取方式有三种：
"""
CSV文件存取：适用于一维二维数组的存取

dat文件存取：适用与多维数组的存取

便捷文件存取：优点：适用于一维二维多维数组的存取，用法最为简单便捷。缺点：保存的文件为二进制文件，该文件里的内容为二进制数据，不利于查看。

"""