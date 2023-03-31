import numpy as np


# ndarray数组切片操作
def test1():
    print("\n")
    a = np.arange(1, 10)
    print(a)  # 1 2 3 4 5 6 7 8 9
    print(a[:3])  # 1 2 3
    print(a[3:6])  # 4 5 6
    print(a[6:])  # 7 8 9
    print(a[::-1])  # 9 8 7 6 5 4 3 2 1
    print(a[:-4:-1])  # 9 8 7
    print(a[-4:-7:-1])  # 6 5 4
    print(a[-7::-1])  # 3 2 1
    print(a[::])  # 1 2 3 4 5 6 7 8 9
    print(a[:])  # 1 2 3 4 5 6 7 8 9
    print(a[::3])  # 1 4 7
    print(a[1::3])  # 2 5 8
    print(a[2::3])  # 3 6 9


# 高维数组切片
def test2():
    print("\n")
    a = np.arange(1, 28)
    a.resize(3, 3, 3)
    print(a)
    # 切出1页
    print(a[1, :, :])
    # 切出所有页的1行
    print(a[:, 1, :])
    # 切出0页的1行1列
    print(a[0, :, 1])

    print(a[::2, 1:2, :1])


# ndarray数组的掩码操作
def test3():
    print("\n")

    # 基于bool数组的掩码
    a = np.arange(1, 11)
    mask = [True, False, True, False, True, False, True, False, True, False]
    print(a[mask])

    # 输出100以内3的倍数
    b = np.arange(100)
    mask = b % 3 == 0
    print(b[mask])
    # print(b[b % 3 == 0])  #简便写法

    # 输出100以内3和7的倍数
    # mask = (b % 3 == 0) and (b%7 == 0)  #报错
    mask = (b % 3 == 0) & (b % 7 == 0)  # 按位与
    print(b[mask])

    print("=====================================")

    # 基于索引的掩码
    # 对品牌做排名
    names = np.array(["vivi", "oppo", "xiaomi", "huawei", "apple"])
    rank = [4, 3, 1, 2, 0]
    print(names[rank])  # ['apple' 'huawei' 'oppo' 'xiaomi' 'vivi']
