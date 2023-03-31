import numpy as np

"""
ndarray类的其他属性
    shape - 维度
    dtype - 元素类型
    size - 元素数量
    ndim - 维数，len(shape)
    itemsize - 元素字节数
    nbytes - 总字节数 = size x itemsize
    real - 复数数组的实部数组
    imag - 复数数组的虚部数组
    T - 数组对象的转置视图
    flat - 扁平迭代器
"""


def test():
    print("\n")
    a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
                  [4 + 2j, 5 + 5j, 6 + 8j],
                  [7 + 3j, 8 + 6j, 9 + 9j]])

    print(a.shape)
    print(a.dtype)
    print(a.ndim)
    print(a.size)
    print(a.itemsize)
    print(a.nbytes)
    print(a.real, a.imag, sep='\n')
    print(a.T)
    print([elem for elem in a.flat])
    b = a.tolist()  # numpy.ndarray  转成 list
    print(b)
    print(type(a))
    print(type(b))
