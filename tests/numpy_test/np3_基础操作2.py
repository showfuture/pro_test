import numpy as np


# ndarray 的属性

def test0():
    # 维度基础操作
    a = np.arange(1, 10)
    print(a, a.shape)
    a.shape = (3, 3)
    print(a, a.shape)
    print(a.dtype)
    # 数据类型的基础操作
    # a.dtype = "float32"  # 强转不靠谱 错误的修改数据类型方式
    # print(a, a.shape, a.dtype)
    b = a.astype("float32")  # 这样是正确的 ，a.astype 是重新生成新的变量b  a是不变的
    print(b, b.shape, b.dtype)
    print(a, a.shape, a.dtype)


# 数组的维度
def test1():
    print("\n")

    ary = np.array([1, 2, 3, 4, 5])
    print(ary, type(ary), ary.shape)
    ary = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print(ary, type(ary), ary.shape)


# 元素的类型
def test2():
    print("\n")
    ary = np.array([1, 2, 3, 4, 5])
    print(ary, type(ary), ary.shape)
    # 转换元素的类型  不会修改原来的数组 只会得到一个新的数组
    b = ary.astype(float)
    print(b, type(b), b.shape)
    c = ary.astype(str)
    print(c, type(c), c.shape)


# 数组元素的个数
def test3():
    print("\n")
    ary = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ])
    print(ary, type(ary), ary.shape)
    print(ary.size)  # 虽然是2维数组 但是是8个元素
    print(len(ary))  # 多维度显示是几维的
    ary = np.array([1, 2, 3, 4, 5])
    print(len(ary))  # 一维的就是当前的数组数量


# 数组元素的索引（下标）
def test4():
    print("\n")
    c = np.arange(1, 19)
    c.shape = (3, 2, 3)  # 3维数组
    print(c)
    print("-" * 10)
    print(c[0])
    print("-" * 10)
    print(c[0][1])
    print("-" * 10)
    print(c[0][0][2])
    print(c[0, 0, 2])  # 两种读取的方式
    print("-" * 10)
    print(c.shape)
