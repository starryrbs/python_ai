## numpy的安装与简单介绍

[原文档](https://blog.csdn.net/qq_41149269/article/details/81221266)
1. 安装numpy

    使用pip

    ```python
    pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

    在文件中导入numpy

    ```python
    import numpy as np
    ```

    np是numpy模块的别名，尽管别名可以省略或更改，建议使用上述约定俗成的别名

2. numpy的N维数组对象：ndarray

    Python已有列表类型,为什么需要一个数组对象(类型)?

    例如: 计算 A^2 +B^3 ,其中,A和B是一维数组。

        a = [0, 1, 2, 3, 4, ]
        b = [9, 8, 7, 6, 5, ]
        
        # 方法1
        def py_sum():
            c = []
            for i in range(len(a)):
                c.append(a[i] ** 2 + b[i] ** 2)
            print(c)
        
        py_sum() #[81, 65, 53, 45, 41]
        
        #方法2
        def np_sum():
            global a
            global b
            a = np.array(a)
            b = np.array(b)
            c = a ** 2 + b ** 2
            print(c)
        np_sum()#[81 65 53 45 41]
    
    对比两种方法:
    
    方法2:
    
    1. 数组对象可以去掉元素间运算所需的循环,使一维向量更像单个数据
    2. 设置专门的数组对象,经过优化,可以提升这类应用的运算速度
    3. 数组对象采用相同的数据类型,有助于节省运算和存储空间
    
    > ndarray是一个多维数组对象，由两部分构成
    
    - 实际的数据
    - 描述这些数据的原数据

    > ndarray对象的属性
    
    - 轴(axis):保存数据的维度；秩(rank):轴的数量
    
       ![img](https://img-blog.csdn.net/20180726163115939?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTQ5MjY5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

    > 实例
	
        # ndarray属性
        
        a = np.array(
            [[1, 2, 3, 4],
             [5, 6, 7, 8]]
        )
        print(a.ndim)  # 秩 2
        print(a.shape)  # 对象的尺度 n行m列 2行4列  (2,4)
        print(a.size)  # 对象的个数 n*m 8
        print(a.dtype)  # 元素类型 int64
        print(a.itemsize)  # 每个元素的大小，以字节为单位  8

    ![img](https://img-blog.csdn.net/20180726164148464?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTQ5MjY5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

    ![img](https://img-blog.csdn.net/20180726164225942?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTQ5MjY5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

    ![img](https://img-blog.csdn.net/20180726164255548?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQxMTQ5MjY5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
    
    > ndarray为什么要支持这么多种元素类型?
    
    - 对比:Python语法仅支持整数、浮点数和复数3种类型
    
        + 科学计算涉及数据较多,对存储和性能都有较高要求
        
        + 对元素类型精细定义,有助于NumPy合理使用存储空间并优化性能
        
        + 对元素类型精细定义,有助于程序员对程序规模有合理评估
        
    > 非同质的ndarray对象：

        a = np.array(
            [[1, 2, 3, 4],
             [5, 6, 7]]
        )
        print(a.ndim)  # 秩 1
        print(a.shape)  # 对象的尺度 n行m列   (2,)
        print(a.size)  # 对象的个数 n*m 2
        print(a.dtype)  # 元素类型 object
        print(a.itemsize)  # 每个元素的大小，以字节为单位  8
    
    - 非同质元素为对象类型
    
    - 非同质的情况下，数组的各种属性已发生变化，与同质情况不同，不必去深究它。
    
    - 非同质ndarray对象无法有效发挥NumPy优势,尽量避免使用