import numpy as np


# 垂直方向操作
def test1():
    print("\n")

    a = np.arange(1, 7).reshape(2, 3)
    b = np.arange(7, 13).reshape(2, 3)
    print(a, b, sep="\n")
    # 垂直方向完成组合操作，生成新数组
    c = np.vstack((a, b))
    print(c)
    # 垂直方向完成拆分操作，生成两个数组
    d, e = np.vsplit(c, 2)
    print(d, e, sep="\n")

    print("=" * 30)


# 水平方向操作
def test2():
    print("\n")
    a = np.arange(1, 7).reshape(2, 3)
    b = np.arange(7, 13).reshape(2, 3)
    print(a, b, sep="\n")
    # 水平方向完成组合操作，生成新数组
    c = np.hstack((a, b))
    print(c)
    # 水平方向完成拆分操作，生成两个数组
    d, e = np.hsplit(c, 2)
    print(d, e, sep="\n")

    print("=" * 30)


# 深度方向操作
def test3():
    print("\n")
    a = np.arange(1, 7).reshape(2, 3)
    b = np.arange(7, 13).reshape(2, 3)
    print(a, b, sep="\n")
    # 深度方向（3维）完成组合操作，生成新数组
    i = np.dstack((a, b))
    print(i)
    # 深度方向（3维）完成拆分操作，生成两个数组
    k, l = np.dsplit(i, 2)
    print(k, l, sep="\n")

    print("=" * 30)


# 多维数组组合与拆分的相关函数
def test4():
    print("\n")
    a = np.arange(1, 28).reshape(3, 3, 3)
    b = np.arange(28, 55).reshape(3, 3, 3)
    print(a, b, sep="\n-----------------------\n")
    # 通过axis作为关键字参数指定组合的方向，取值如下：
    # 若待组合的数组都是二维数组：
    # 0: 垂直方向组合
    # 1: 水平方向组合
    # 若待组合的数组都是三维数组：
    # 0: 垂直方向组合
    # 1: 水平方向组合
    #  2: 深度方向组合
    print("\n-----------------------")
    c = np.concatenate((a, b), axis=2)
    print(c)
    print("\n-----------------------")
    # 通过给出的数组与要拆分的份数，按照某个方向进行拆分，axis的取值同上
    d, e = np.split(c, 2, axis=2)
    print(d, e, sep="\n-----------------------\n")


# 长度不等的数组组合
def test5():
    print('\n')
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 4])
    # 填充b数组使其长度与a相同 头部补0个元素，尾部补1个元素
    # mode='constant' 补常量
    # constant_values=-1 常量的值是-1
    b = np.pad(b, pad_width=(0, 1), mode='constant', constant_values=-1)
    print(b)
    # 垂直方向完成组合操作，生成新数组
    c = np.vstack((a, b))
    print(c)

# 简单的一维数组组合方案
def test6():
    print('\n')
    a = np.arange(1, 9)  # [1, 2, 3, 4, 5, 6, 7, 8]
    b = np.arange(9, 17)  # [9,10,11,12,13,14,15,16]
    # 把两个数组摞在一起成两行
    c = np.row_stack((a, b))
    print(c)
    # 把两个数组组合在一起成两列
    d = np.column_stack((a, b))
    print(d)