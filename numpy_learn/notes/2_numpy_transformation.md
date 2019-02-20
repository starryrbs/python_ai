## ndarray数组的创建与转换
[原文档](https://blog.csdn.net/qq_41149269/article/details/81224111)


1. ndarray数组的创建

    1. 方法1

        ```python
        x = np.array(list/tuple)
        x = np.array(list/tuple, dtype=np.float32)
        ```

        不指定参数dtype时，numpy将根据数据的情况关联一个dtype类型

        从python中的列表元祖创建

            a = np.array([1, 2, 3])
            print(a)#[1 2 3]
            
            # 从元祖类型创建
            b = np.array((1, 2, 3))
            print(b)#[1 2 3]
            
            # 从列表和元祖的混合类型创建
            c = np.array([[1, 2], [2, 3, 4], (1, 2, 3)])
            
            print(c)#[list([1, 2]) list([2, 3, 4]) (1, 2, 3)]

    2. 方法2

        使用numpy中函数创建ndarray数组，如：arange, ones, zeros等
        
        - 使用np.arange(n)函数创建,类似ndarray类型，元素从0到n-1

                a = np.arange(10)
                print(a)  # [0 1 2 3 4 5 6 7 8 9]
            
        -  使用np.ones(shape)函数:根据shape生成一个元素全为1的数组,shape是元祖类型
            没有指定dtype,默认为浮点型
            
                #   创建一个2行4列的ndarray
                a = np.ones((2, 4))
                print(a)
                
                [[1. 1. 1. 1.]
                [1. 1. 1. 1.]]
                
                # 创建一个多维数组,可以理解为2个3行4列的数组
                a = np.ones((2, 3, 4), dtype=np.int64)
                print(a)
                
                [[[1 1 1 1]
                  [1 1 1 1]
                  [1 1 1 1]]
        -  使用np.zeros(shape)函数:根据shape生成一个元素全为0的数组，shape是元祖类型
           没有指定dtype,默认为浮点型
           
                a = np.zeros((2, 4))
                print(a)
                
                [[0. 0. 0. 0.]
                [0. 0. 0. 0.]]
           
        -  使用np.full(shape,val)函数:根据shape生成一个数组，每个元素值均为val,shape是元祖类型
            创建一个3行4列值全为2的ndarray
            
                a = np.full((3, 4), 2)
                print(a)
                
                [[2 2 2 2]
                 [2 2 2 2]
                 [2 2 2 2]]
            
        -  使用np.eye(n)函数:创建一个正方形的n*n单位矩阵,

                a = np.eye(4)
                print(a)
                
                [[1. 0. 0. 0.]
                 [0. 1. 0. 0.]
                 [0. 0. 1. 0.]
                 [0. 0. 0. 1.]]
            
        > 拓展：

        + np.ones_like(a) ：根据数组a的形状生成一个元素全为1的数组；
        
        + np.zeros_like(a) ：根据数组a的形状生成一个元素全为0的数组；
        
        + np.full_like(a，val) ：根据数组a的形状生成一个元素全为val的数组；
        
    3. 方法3，使用numpy其它的一些方法，例如linspace,concatenate

       1. np.linspace() : 根据起止数据等间距地填充数据，形成数组
          
                a = np.linspace(2, 8, 3, dtype=np.int32)
                print(a)  # [2 5 8]
            
       2. 合并两个或多个数组
       
                c = np.concatenate((np.array([1, 2]), np.array([2, 3])))
                print(c)  # [1 2 2 3]

2. 数组的转换

    1. 维度转换
    
        - reshape(shape)：不改变数组元素，返回一个shape形状的数组，原数组不变。

                a = np.zeros((2, 4))
                print(a)
                """
                [[0. 0. 0. 0.]
                 [0. 0. 0. 0.]]
                """
                b = a.reshape((1, 8))
                print(b)
                """
                [[0. 0. 0. 0. 0. 0. 0. 0.]]
                """
                # shape是变的，size是不变的,也就是2×4 = 1*8,否则报错

        - resize(shape)：不改变数组元素，不返回一个shape形状的数组，而且原数组元素改变。

                a = np.full((2,3),5)
                print(a)
                """
                [[5 5 5]
                 [5 5 5]]
                """
                a.resize((2,8))
                print(a)
                """
                [[5 5 5 5 5 5 0 0]
                 [0 0 0 0 0 0 0 0]]
                """
            
        - flatten()：对数组进行降维，返回折叠后的一维数组，原数组不变

                a=np.eye(4)
                print(a)
                print(a.flatten())
        
    2. 类型转换
    
        - 元素类型的变换：
        
                a = np.ones((1, 2), dtype=np.int)
                print(a)  # [[1 1]]
                print(a.astype(np.float))  # [[1. 1.]]
            
        - 数组向列表的转换：
        
                a = np.full((2, 3), 10)
                print(a)
                """
                [[10 10 10]
                [10 10 10]]
                """
                print(a.tolist())
                """
                [[10, 10, 10], [10, 10, 10]]
                """