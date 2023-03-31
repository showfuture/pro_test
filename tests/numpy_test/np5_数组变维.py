import numpy as np


def test1():
    print("\n")
    # 视图变维（数据共享）： reshape() 与 ravel()
    # 只是维度不一样，数据是一样的
    a = np.arange(1, 9)
    print(a)  # [1 2 3 4 5 6 7 8]
    b = a.reshape(2, 4)  # 视图变维  : 变为2行4列的二维数组
    print(b)
    a[0] = 999  # 修改以后再得到的数据会变， 但是上边的b不会变， 因为是在改之前得到的b
    c = b.reshape(2, 2, 2)  # 视图变维    变为2页2行2列的三维数组
    print(c)
    d = c.ravel()  # 视图变维 和flatten类似	变为1维数组
    print(d)
    print("=" * 30)

    # 复制变维（数据独立）： flatten()
    # 维度改成一维数组， 新得到的数组和以前的是不一样的，各是各的
    e = c.flatten()
    print(e)
    c += 10
    print(a, e, sep='\n')
    print("=" * 30)

    # 就地变维：直接改变原数组对象的维度，不返回新数组
    a.shape = (2, 4)
    print(a)
    a.resize(2, 2, 2)
    print(a)


def test2():
    print("\n")
    a = [1, 2, 3, 4, 5]
    print(a)
    a[0] = 99
    b = a
    print(b)


def test3():
    print("\n")

    def mul():
        return [lambda x: x * i for i in range(4)]

    print([m(2) for m in mul()])

    """
    以上这段代码输出的结果是[6, 6, 6, 6]，而不是[0, 2, 4, 6]！
    产生这个问题的原因在于Python闭包的延迟绑定。这意味着内部函数被调用时，
    参数的值在闭包内进行查找。所以当mul()返回的函数被调用时，
    i的值会在返回的函数里查找，而for循环完成后i的值为3，也就是i最终赋值为3。
    因此，每次返回的函数乘以传入的值就是最后的结果，得到的结果就是[6, 6, 6, 6]。
    """
    print('=====================================')

    def mul1():
        for i in range(4):
            yield lambda x: x * i

    print([m(2) for m in mul1()])

    print('=====================================')

    def mul2():
        return [lambda x, i=i: x * i for i in range(4)]

    print([m(2) for m in mul2()])
