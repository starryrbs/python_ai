## numpy数组的操作和运算
[原文档](https://blog.csdn.net/qq_41149269/article/details/81226955)

1. 数组的索引和切片

    - numpy数组也可以切片和索引

        ```python
        a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        # 索引
        print(a[0])  # 1
        # 切片
        print(a[0:-1:2])  # [1 3 5 7]
        ```

    - 多维数组的索引

        ```python
        # 索引：每个维度一个索引值，逗号分割
        a = np.arange(0, 20).reshape(2, 2, 5)
        print(a)
        """
        [[[ 0  1  2  3  4]
          [ 5  6  7  8  9]]
        
         [[10 11 12 13 14]
          [15 16 17 18 19]]]
        """
        # 取元素19
        print(a[1, 1, -1])  # 19
        # 取元素7
        print(a[0, 1, 2])
        ```

    - 多维数组的切片

        ```python
        # 切片
        a = np.arange(0, 20).reshape(2, 2, 5)
        print(a)
        """
        [[[ 0  1  2  3  4]
          [ 5  6  7  8  9]]
        
         [[10 11 12 13 14]
          [15 16 17 18 19]]]
        
        """
        # 切片取7到9个元素
        print(a[0, 1, 2:])#[7 8 9]
        # 切片取7,8,17,18四个元素
        print(a[:, 1, 2:4])
        """
        [[ 7  8]
         [17 18]]
        """
        # 切片取7,9两个元素
        print(a[0, 1, 2::2])
        #[7 9]
        ```

2. ndarray数组的运算     

    - 数组与标量之间的运算：数组与标量之间的运算作用于数组的每一个元素

        ```python
        a = np.arange(24).reshape((2, 3, 4))
        print(a)
        """
        [[[ 0  1  2  3]
          [ 4  5  6  7]
          [ 8  9 10 11]]
        
         [[12 13 14 15]
          [16 17 18 19]
          [20 21 22 23]]]
        """
        # 求数组a的平均值即求数组a内元素的平均值：
        print(a.mean())  # 11.5
        # 计算a与元素平均值的商：
        a = a / a.mean()
        print(a)
        """
        [[[0.         0.08695652 0.17391304 0.26086957]
          [0.34782609 0.43478261 0.52173913 0.60869565]
          [0.69565217 0.7826087  0.86956522 0.95652174]]
        
         [[1.04347826 1.13043478 1.2173913  1.30434783]
          [1.39130435 1.47826087 1.56521739 1.65217391]
          [1.73913043 1.82608696 1.91304348 2.        ]]]
        """
        ```
    - numpy的一元函数

        + np.abs(x)或np.fabs(x) :  计算数组各元素的绝对值

        + np.sqrt(x)：计算数组各元素的平方根

        + np.square(x): 计算数组各元素的平方

        + np.log(x)   np.log10(x)  np.log2(x)  :  分别表示数组各元素的自然对数、以10为底的对数、以2为底的对数

        + np.ceil(x)  np.floor(x)  :   ceil中文为天花板，即朝正无穷大方向取整；floor中文为地板，即朝负无穷大方向取整

            > 举例 

            ```python
            a = np.array([0.2, 0.8, 1.2])
            print(np.ceil(a))  # [1. 1. 2.]
            ```

        + np.rint(x) : 计算数组各元素的四舍五入值

        + np.modf(x) : 将数组各元素的小数和整数部分以两个独立数组形式返回

        + np.cos(x)  np.cosh(x)  np.sin(x)  np.sinh(x)  np.tan(x)  np.tanh(x)  :  计算数组各元素的普通型和双曲型三角函数

        + np.exp(x) ：计算数组各元素的指数值

        + np.sign(x) ：计算数组各元素的符号值，1(+)，0，-1(-)

            ```python
            a = np.array([2, 3, -4, 5])
            print(np.sign(a))  # [ 1  1 -1  1]
            print(np.modf(a))  # (array([ 0.,  0., -0.,  0.]), array([ 2.,  3., -4.,  5.]))
            print(np.square(a))  # [ 4  9 16 25]
            ```

    - 二元函数

        + \+ - * /  **   :    两个数组各元素进行对应运算

        + np.maximun(x,y) 或np.fmax() :  元素级的最大值

        + np.minimun(x,y) 或np.fmin() :   元素级的最小值

        + np.mod(x, y) :  元素级的模运算

        + np.copysign(x, y) :  将数组y中各元素值的符号赋值给数组x对应的元素

        + \>  <  >=  <=  ==  !=   :   算术比较，产生布尔型数组

            ```python
            a = np.arange(24).reshape((2, 3, 4))
            print(a)
            """
            [[[ 0  1  2  3]
              [ 4  5  6  7]
              [ 8  9 10 11]]
            
             [[12 13 14 15]
              [16 17 18 19]
              [20 21 22 23]]]
            """
            b = np.arange(-12, 12).reshape((2, 3, 4))
            print(b)
            """
            [[[-12 -11 -10  -9]
              [ -8  -7  -6  -5]
              [ -4  -3  -2  -1]]
            
             [[  0   1   2   3]
              [  4   5   6   7]
              [  8   9  10  11]]]
            """
            print(np.maximum(a, b))
            """
            [[[ 0  1  2  3]
              [ 4  5  6  7]
              [ 8  9 10 11]]
            
             [[12 13 14 15]
              [16 17 18 19]
              [20 21 22 23]]]
            """
            
            print(a+b)
            """
            [[[-12 -10  -8  -6]
              [ -4  -2   0   2]
              [  4   6   8  10]]
            
             [[ 12  14  16  18]
              [ 20  22  24  26]
              [ 28  30  32  34]]]
            """
            ```

