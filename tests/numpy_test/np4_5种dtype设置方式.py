import numpy as np


def test1():
    print('\n')
    # 姓名  语数外分数， 年龄
    data = [
        ("zsss", [39, 89, 60], 19),
        ("ls", [50, 30, 90], 20),
        ("ww", [89, 98, 87], 21),
    ]

    # 第一种设置dtype的方式
    # U2表示Unicode类型出现2个， 如果文字过多，但是U2过短，只会按照U2的长度进行截取
    # 3int32 表示3个int32的数据
    # dtype如果把数据类型定死，这些数据占的内存就是固定的
    ary = np.array(data, dtype="U2, 3int32, int32")
    print(ary)
    print(ary[1][1])
    print("-" * 30)

    # 第二种设置dtype的方式 ("name", "str", 2) 对应 （别名， 类型， 个数）
    ary = np.array(data, dtype=[
        ("name", "str", 2),
        ("score", "int32", 3),
        ("age", "int32", 1)
    ])
    print(ary)
    print(ary["name"])
    print(ary["score"])
    print(ary["age"])
    print(ary[2]["age"])
    print("-" * 30)

    # 第三种设置dtype的方式
    # names formats 是固定写法
    ary = np.array(data, dtype={
        "names": ["name", "score", "age"],
        "formats": ["U2", "3int32", "int32"]
    })

    print(ary)
    print(ary["name"])
    print(ary["score"])
    print(ary["age"])
    print(ary[2]["age"])
    print("-" * 30)

    # 第四种设置dtype的方式
    # (U3, 0) 表示内存偏移量从0开始，U3,3个4字节，总共使用12, 使用的位置是0-12
    # (3int32, 16) 表示内存偏移量从16开始，U3,3个4字节，总共使用12, 使用的位置是16-28
    # (int32, 28)  表示内存偏移量从28开始，int32是个4字节，总共使用4, 使用的位置是28-32
    # 通过这些来实际控制数据的内存使用量，增加读取效率
    d = np.array(data, dtype={'names': ('U3', 0),
                              'scores': ('3int32', 16),
                              'ages': ('int32', 28)})
    print(d[0]['names'], d[0]['scores'])
    print("itemsize", d.itemsize)  # 获取占用内存

    print("=====================================")

    # 第五种设置dtype的方式
    # 偏底层
    e = np.array([0x1234, 0x5667],
                 dtype=('u2', {'lowc': ('u1', 0),
                               'hignc': ('u1', 1)}))
    print('%x' % e[0])
    print('%x %x' % (e['lowc'][0], e['hignc'][0]))

    print("=====================================")

    # 测试日期类型数组
    f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01', '2011-02-01'])
    print(f, f.dtype)
    f = f.astype('M8[D]')  # D保留到天
    # f = f.astype('M8[s]')  # s保留到秒
    print(f[3] - f[0])  # 日期的计算
    print(f)
    f = f.astype('int32')  #
    print(f)
    print(f[3] - f[0])

    print("=====================================")
    a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
                  [4 + 2j, 5 + 5j, 6 + 8j],
                  [7 + 3j, 8 + 6j, 9 + 9j]])
    print(a.T)

    for x in a.flat:
        print(x.imag)

