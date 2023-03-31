import numpy as np


def test1():
    print("\n")
    # 创建np array的两个方法
    # 1
    ary1 = np.array([1, 2, 3, 4, 5])
    print(ary1, type(ary1))
    # 2  arange(起始值，终止值， 步长）
    ary2 = np.arange(1, 10, 2)
    print(ary2)


def test2():
    print("\n")
    # 生成全为0的数组， 可以指定类型
    ary1 = np.zeros(10, dtype=bool)
    print(ary1)
    ary2 = np.zeros(10, dtype="int32")
    print(ary2)

    # 生成全为1的数组，可以指定类型
    ary3 = np.ones(10, dtype=str)
    print(ary3)

    ary4 = np.ones((2, 5), dtype="float")
    print(ary4, ary4.shape, ary4.dtype)

    ary5 = np.ones((2, 5), dtype="str")
    print(ary5, ary5.shape, ary5.dtype)

    # 得到5个 1/5
    print(np.ones(5) / 5)

    # 得到类似某个数组的维度 的数组，全是0 或者全是1
    print(np.zeros_like(ary4))
    print(np.ones_like(ary5))
