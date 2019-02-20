import numpy as np

a = [0, 1, 2, 3, 4, ]
b = [9, 8, 7, 6, 5, ]


def py_sum():
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 2)
    print(c)


# py_sum()


def np_sum():
    global a
    global b
    a = np.array(a)
    b = np.array(b)
    c = a ** 2 + b ** 2
    print(c)


# np_sum()

# ndarray属性

a = np.array( 
    [[1, 2, 3, 4],
     [5, 6, 7]]
)
print(a.ndim)  # 秩 1
print(a.shape)  # 对象的尺度 n行m列   (2,)
print(a.size)  # 对象的个数 n*m 2
print(a.dtype)  # 元素类型 object
print(a.itemsize)  # 每个元素的大小，以字节为单位  8
