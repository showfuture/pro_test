import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])


def test1():
    print("\n")
    print(ary)
    print(type(ary))
    # shape: 维度 （6，）
    print(ary.shape)


def test2():
    print("\n")
    ary.shape = (2, 3)  # 维度改为两行三列
    print(ary)
    print(ary.shape, ary.size, ary.dtype)  # (2, 3)  6 int32


def test3():
    print("\n")
    ary.shape = (6,)
    print(ary)
    print(ary * 3)  # 可以直接做运算
    print(ary > 3)  # [False False False  True  True  True]
    print(ary + ary)  # [ 2  4  6  8 10 12]


def test4():
    print("\n")
    print("----" * 4)
    ary1 = np.array([1, 2, 3, 4, 5, 6])
    ary2 = np.array([1, 2, 3, 4, 5])
    print(ary1 + ary2)  # 维度不一致不能做运算  会报错
