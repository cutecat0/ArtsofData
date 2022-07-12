import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from collections import namedtuple


"""
    Reference: https://pandas.pydata.org/docs/user_guide/dsintro.html
"""


def series_from_ndarray():
    """
    A  Series is one-dimensional labeled array.
    s = pd.Series(data, index=index)
    """
    # 1. From ndarray
    # If data is ndarray, index must be the same length as data.
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    print(s)
    """
    a   -0.261770
    b   -0.164276
    c    0.590781
    d   -1.468494
    e   -0.107874
    dtype: float64
    """
    print(s.index)
    " Index(['a', 'b', 'c', 'd', 'e'], dtype='object') "

    # when data is ndarray-like, and U want it to be real ndarray, use the follow
    s.to_numpy()
    # Out[13]: array([-0.39385148, -0.93355423,  1.1051972 ,  0.71894043, -0.21014577])

    # a series which is like a fixed_size dict, U can get and set values by index label
    print(s["a"], s["e"])
    # -0.006321635835820239 0.8299959086276444
    s["e"] = 0.66666
    print(s["e"])
    # 0.66666

    # Using the get(), the missing label will turn None or, set a special default
    s.get("f")
    s.get("e")
    # Out[3]: 1.169925222834734
    s.get("f", np.nan)
    # Out[4]: nan
    """
    s + s
    Out[2]:
    a   -1.569224
    b    0.829274
    c   -0.464486
    d   -3.408521
    e   -3.003048
    dtype: float64
    s * 2
    Out[3]:
    a   -1.569224
    b    0.829274
    c   -0.464486
    d   -3.408521
    e   -3.003048
    dtype: float64
    np.exp2(s)
    Out[4]:
    a    0.580508
    b    1.332963
    c    0.851310
    d    0.306878
    e    0.353180
    dtype: float64
    
    s[1:] + s[:-1]
    Out[5]: 
    a         NaN
    b    0.829274
    c   -0.464486
    d   -3.408521
    e         NaN
    dtype: float64
    """

    s2 = pd.Series(np.random.randn(5), name="magic")
    print(s2)
    """
    0    0.409252
    1    0.338865
    2    0.818272
    3   -0.247809
    4    0.589885
    Name: magic, dtype: float64
    """
    s3 = s2.rename("MagicData")
    print(s3, '\n', s3.name)
    """
    0   -2.005633
    1   -1.640921
    2   -0.041737
    3   -1.053985
    4    0.388305
    Name: MagicData, dtype: float64 
     MagicData
    """

    brk = 1


def series_from_dict():
    """
    When the data is a dict and index isn't passed, the index of Series will be ordered by the dict's insertion order.
    """
    dic = {"cat": 100, "Duck": 98, "Rabbit": 88}
    s = pd.Series(dic)

    print(s)
    """
    cat       100
    Duck       98
    Rabbit     88
    dtype: int64
    """
    """ If an index is passed, the values in the dict will be instead of by passed index """
    s2 = pd.Series(dic, index=["cat", "Duck", "r", "o"])
    print(s2)
    """
    cat     100.0
    Duck     98.0
    r         NaN
    o         NaN
    dtype: float64
    """
    # NaN(Not a Number) is the standard missing data marker used in pandas


def series_from_scalar_value():
    """
    If the data is a scalar value, the index must be provided, the value will be repeated to match the length of index
    """
    s = pd.Series(6.6, index=["a", "b", "c", "d", "e", "f"])
    print(s)
    """
    a    6.6
    b    6.6
    c    6.6
    d    6.6
    e    6.6
    f    6.6
    dtype: float64
    """


def dataframe_from_dicts_of_series():
    """
    A DataFrame is 2D(Dimensional) labeled Sstruct Data Type
    Index(row), 行
    Columns(columns) 列
    """
    pet = {
        "cat": pd.Series([1.0, 2.0, 3.0], index=["food", "weight", "cute"]),
        "duck": pd.Series([1.0, 2.0, 3.0, 4.0], index=["food", "weight", "cute", "water"])
    }

    df = pd.DataFrame(pet)

    print(df)
    """
            cat  duck
    cute    3.0   3.0
    food    1.0   1.0
    water   NaN   4.0
    weight  2.0   2.0
    """

    # df.columns
    # Out[3]: Index(['cat', 'duck'], dtype='object')
    # df.index
    # Out[4]: Index(['cute', 'food', 'water', 'weight'], dtype='object')


def df_from_dict_of_ndarry_or_list():
    """
    The ndarray must be the same length. If the index is passed, it must be cleary and also the same length as the array.
    """

    pets = {
        "cat": [1.0, 2.0, 3.0, 4.0],
        "duck": [4.0, 4.0, 2.0, 1.0]
    }

    df = pd.DataFrame(pets)

    print(df)
    """
       cat  duck
    0  1.0   4.0
    1  2.0   4.0
    2  3.0   2.0
    3  4.0   1.0
    """

    df = pd.DataFrame(pets, index=["weight", "food", "water", "name"])
    # index here is the name of rows.
    print(df)
    """
            cat  duck
    weight  1.0   4.0
    food    2.0   4.0
    water   3.0   2.0
    name    4.0   1.0
    """


def df_from_structured_or_record_array():
    data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10")])
    data[:] = [(1, 2, "Cat"), (3, 4, "Duck")]
    print(data)
    " [(1, 2., b'Cat') (3, 4., b'Duck')]  "  # ???

    df = pd.DataFrame(data)
    print(df)
    # ??? Why why why why ???
    """
       A    B        C
    0  1  2.0   b'Cat'
    1  3  4.0  b'Duck'
    """

    # from list of dicts

    data2 = [{"a": 1, "b": 2}, {"a": 6, "b": 8, "c": 10}]
    df = pd.DataFrame(data2)
    print(df)
    """
       a  b     c
    0  1  2   NaN
    1  6  8  10.0
    """

    df2 = pd.DataFrame(data2, index=["row1", "row2"])
    print(df2)
    """
          a  b     c
    row1  1  2   NaN
    row2  6  8  10.0
    """

    df3 = pd.DataFrame(data2, columns=["a", "b"])
    print(df3)
    """
       a  b
    0  1  2
    1  6  8
    """

    # from dict of tuples
    data3 = {
        ("a", "b"): {("A", "B"): 1, ("B", "C"): 2},
        ("a", "a"): {("A", "A"): 6, ("B", "B"): 12},
        ("a", "c"): {("A", "C"): 24, ("B", "A"): 48},
        ("b", "c"): {("A", "C"): 32, ("A", "C"): 96}
    }

    df = pd.DataFrame(data3)
    print(df)
    # Why ??? What happened ???
    """
           a                 b
           b     a     c     c
    A B  1.0   NaN   NaN   NaN
    B C  2.0   NaN   NaN   NaN
    A A  NaN   6.0   NaN   NaN
    B B  NaN  12.0   NaN   NaN
    A C  NaN   NaN  24.0  96.0
    B A  NaN   NaN  48.0   NaN
    """

    # from namedtuple
    Point = namedtuple("Point", "x y")
    print(Point)
    # <class '__main__.Point'>
    df = pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)])
    print(df)
    """
       x  y
    0  0  0
    1  0  3
    2  2  3
    """

    Point3D = namedtuple("Point3D", "x y z")
    df = pd.DataFrame([Point3D(0, 0, 0), Point3D(1, 3, 5), Point(6, 88)], index=["row1", "row2", "row3"])
    print(df)
    """
          x   y    z
    row1  0   0  0.0
    row2  1   3  5.0
    row3  6  88  NaN
    """


def df_from_dict():
    df = pd.DataFrame.from_dict(dict([('cat', [1, 11, 111]), ('duck', [2, 22, 222])]))
    print(df)
    """
       cat duck
    0    1    2
    1   11   22
    2  111  222
    """
    df2 = pd.DataFrame.from_dict(
        dict([('cat', [1, 11, 111]), ('duck', [2, 22, 222])]),
        orient='index',
        columns=['col1', 'col2', 'col3'])
    print(df2)
    """
         col1 col2 col3
    cat     1   11  111
    duck    2   22  222
    """

    """
    data
    Out[67]: 
    array([(1, 2., b'Hello'), (2, 3., b'World')],
          dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])
    
    pd.DataFrame.from_records(data, index="C")
    Out[68]: 
              A    B
    C               
    b'Hello'  1  2.0
    b'World'  2  3.0
    """
    df['cute'] = df['cat'] * df['duck']
    df['flag'] = df['cute'] > 10
    print(df)
    """
       cat  duck   cute   flag
    0    1     2      2  False
    1   11    22    242   True
    2  111   222  24642   True
    """

    del df['duck']
    cute = df.pop('cute')
    print(df, '\n', cute)
    """
       cat   flag
    0    1  False
    1   11   True
    2  111   True 
    
    0        2
    1      242
    2    24642
    Name: cute, dtype: int64
    """

    df['dog'] = 'wow'
    print(df)
    """
       cat   flag  dog
    0    1  False  wow
    1   11   True  wow
    2  111   True  wow
    """

    df['smart'] = df['cat'][:2]
    print(df)
    """
       cat   flag  dog  smart
    0    1  False  wow    1.0
    1   11   True  wow   11.0
    2  111   True  wow    NaN
    """

    df.insert(1, 'cute', df['cat'])
    print(df)
    """
       cat  cute   flag  dog  smart
    0    1     1  False  wow    1.0
    1   11    11   True  wow   11.0
    2  111   111   True  wow    NaN
    """


def assigning_df():
    iris = pd.read_csv('data/iris.csv')
    print(iris.head())
    """
       sepal_length  sepal_width  petal_length  petal_width species
    0           5.1          3.5           1.4          0.2  setosa
    1           4.9          3.0           1.4          0.2  setosa
    2           4.7          3.2           1.3          0.2  setosa
    3           4.6          3.1           1.5          0.2  setosa
    4           5.0          3.6           1.4          0.2  setosa
    """
    print(iris.assign(sepal_ratio=iris['sepal_width'] / iris['sepal_length']).head())
    """
       sepal_length  sepal_width  petal_length  petal_width species  sepal_ratio
    0           5.1          3.5           1.4          0.2  setosa     0.686275
    1           4.9          3.0           1.4          0.2  setosa     0.612245
    2           4.7          3.2           1.3          0.2  setosa     0.680851
    3           4.6          3.1           1.5          0.2  setosa     0.673913
    4           5.0          3.6           1.4          0.2  setosa     0.720000
    """
    print(iris.assign(sepal_ratio=lambda x: (x['sepal_width'] / x['sepal_length'])).head())
    """
       sepal_length  sepal_width  petal_length  petal_width species  sepal_ratio
    0           5.1          3.5           1.4          0.2  setosa     0.686275
    1           4.9          3.0           1.4          0.2  setosa     0.612245
    2           4.7          3.2           1.3          0.2  setosa     0.680851
    3           4.6          3.1           1.5          0.2  setosa     0.673913
    4           5.0          3.6           1.4          0.2  setosa     0.720000
    """

    fig, ax = plt.subplots()
    (
        iris.query('sepal_length > 5')
        .assign(
            sepal_ratio=lambda x: x.sepal_width / x.sepal_length,
            petal_ratio=lambda x: x.petal_width / x.petal_length,
        )
        .plot(kind='scatter', x='sepal_ratio', y='petal_ratio')
    )
    plt.grid()
    plt.show()

    dfa = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['row_a', 'row_b', 'row+c'])
    """
           A  B
    row_a  1  4
    row_b  2  5
    row+c  3  6
    """
    print(dfa.assign(C=lambda x: x['A'] + x['B'], D=lambda x: x['A'] + x['C']))
    """
       A  B  C   D
    0  1  4  5   6
    1  2  5  7   9
    2  3  6  9  12
    """

    # get column use df[col]
    """
    dfa['A']
    Out[4]:
    row_a    1
    row_b    2
    row+c    3
    Name: A, dtype: int64
    """

    # get row use df.loc[row]
    """
    dfa.loc['row_a']
    Out[5]: 
    A    1
    B    4
    Name: row_a, dtype: int64
    """

    # get row through index loc
    """
    dfa.iloc[1]
    Out[7]: 
    A    2
    B    5
    Name: row_b, dtype: int64
    dfa.iloc[0]
    Out[8]: 
    A    1
    B    4
    Name: row_a, dtype: int64
    """

    # col slice use df[1:5]
    """
    dfa[2:3]
    Out[10]: 
           A  B
    row+c  3  6
    dfa[1:2]
    Out[11]: 
           A  B
    row_b  2  5
    """


def df_alignment_arithmetic():

    df1 = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
    df2 = pd.DataFrame(np.random.randn(7, 3), columns=["A", "B", "C"])

    df3 = df1 + df2
    print(df3)
    """
              A         B         C   D
    0  1.555039  0.754134 -0.479506 NaN
    1  2.168825  0.510122 -0.717997 NaN
    2  0.972565 -0.254369  0.427732 NaN
    3 -0.043925 -4.047558 -0.844054 NaN
    4  3.256367  0.964496 -1.166407 NaN
    5  1.043344  0.252463 -2.664283 NaN
    6  0.414339 -1.116950  0.313440 NaN
    7       NaN       NaN       NaN NaN
    8       NaN       NaN       NaN NaN
    9       NaN       NaN       NaN NaN
    """

    print(df1)
    """
              A         B         C         D
    0 -0.529329 -0.248560 -0.317801  0.186850
    1  0.259817 -1.142044  1.433382 -0.339876
    2 -0.252119  0.179474 -0.649148 -1.644756
    3  0.389451  1.355463  0.044246  0.356374
    4  0.311718 -0.496003  0.454940 -0.888060
    5  0.041785 -0.548488  0.026349  1.595006
    6 -1.615808 -0.690391 -0.351577  1.412334
    7 -1.281519  0.708204  0.195342  0.635574
    8  1.187066 -0.168230 -0.766493 -0.541688
    9  0.043890 -0.030780 -1.891522 -2.471875
    """
    print(df1 - df1.iloc[0])
    """
              A         B         C         D
    0  0.000000  0.000000  0.000000  0.000000
    1  0.789146 -0.893484  1.751183 -0.526726
    2  0.277210  0.428034 -0.331347 -1.831605
    3  0.918779  1.604023  0.362047  0.169524
    4  0.841047 -0.247443  0.772741 -1.074910
    5  0.571114 -0.299928  0.344150  1.408156
    6 -1.086479 -0.441831 -0.033776  1.225484
    7 -0.752190  0.956764  0.513143  0.448724
    8  1.716395  0.080330 -0.448692 -0.728538
    9  0.573219  0.217780 -1.573721 -2.658725
    """
    print(df1 * 5 + 2)
    """
               A         B         C         D
    0  -0.543389  8.091031  5.227662  4.082398
    1   2.367068  3.079644  5.686881  3.496078
    2   5.790306  2.621025  5.724741  4.414219
    3  10.556532 -3.206337 -4.649103  7.595489
    4   1.552070  1.005933  6.945729  0.600131
    5  11.051991  2.119194  3.393111  1.345669
    6   3.346961 -1.706559 -0.528637 -1.430357
    7   3.646620 -0.782593  4.095359  1.449749
    8  -0.352574 -1.228543  1.411770  0.958920
    9   0.588579 -2.519251 -1.062918  5.477413
    """
    print(1 / df1)
    """
              A         B         C          D
    0  1.543549 -2.854639 -1.711020  -1.057494
    1  0.756624  2.003680 -1.457544  -2.313737
    2 -1.222379 -4.190857 -0.676878  -2.672541
    3  3.114492  3.096253 -5.375483 -39.454023
    4  2.569083 -0.767821  0.943320   2.338810
    5  0.874833 -2.214583  1.359369   0.344772
    6 -0.591150 -0.816738  0.812004   0.654312
    7 -0.956595 -1.157327  2.010167   0.298145
    8  2.815532 -3.468471 -1.296206  10.795007
    9  0.722981  3.087660  1.096971  -2.844795
    """
    print(df1 ** 4)
    """
               A          B             C             D
    0   8.531958   0.015782  1.315774e-01  3.586171e-04
    1   5.349168   0.008885  5.072501e-04  3.253917e+00
    2   0.065909   0.035949  1.255652e-05  1.308820e-01
    3   0.015177   0.042075  1.062882e-01  8.747363e-01
    4   0.251582  11.364179  1.907325e-07  1.243413e-05
    5   0.126790   0.022078  2.181311e-03  3.666460e-09
    6   0.922587   0.048575  3.099112e-01  8.624552e-02
    7  15.135800   2.739634  1.474514e+01  4.088397e-04
    8   9.271338   0.001131  4.981402e-01  4.167985e+00
    9   0.000102   0.015707  5.222039e-06  7.392714e-01
    """


def bool_df():
    df1 = pd.DataFrame({'a': [1, 0, 1], 'b': [0, 1, 1]}, dtype=bool)
    df2 = pd.DataFrame({'a': [0, 1, 1], 'b': [1, 1, 0]}, dtype=bool)
    print(df1, '\n', df2)
    """
           a      b
    0   True  False
    1  False   True
    2   True   True 
            a      b
    0  False   True
    1   True   True
    2   True  False
    """
    print(df1 & df2)
    """
           a      b
    0  False  False
    1  False   True
    2   True  False
    """
    print(df1 | df2)
    """
          a     b
    0  True  True
    1  True  True
    2  True  True
    """
    print(df1 ^ df2)
    """
           a      b
    0   True   True
    1   True  False
    2  False   True
    """
    print(~df1)
    """
           a      b
    0  False   True
    1   True  False
    2  False  False
    """


if __name__ == '__main__':
    # series_from_ndarray()
    """
    s[0]
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.20.0 -- An enhanced Interactive Python. Type '?' for help.
    PyDev console: using IPython 7.20.0
    Out[1]: -0.3938514756551117
    s[:3]
    Out[2]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    dtype: float64
    s[s > s.median()]
    Out[3]: 
    c    1.105197
    d    0.718940
    dtype: float64
    s
    Out[4]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    d    0.718940
    e   -0.210146
    dtype: float64
        s[[4, 3, 1]]
    Out[6]: 
    e   -0.210146
    d    0.718940
    b   -0.933554
    dtype: float64
    np.exp(s)
    Out[7]: 
    a    0.674454
    b    0.393154
    c    3.019820
    d    2.052258
    e    0.810466
    dtype: float64
    s
    Out[8]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    d    0.718940
    e   -0.210146
    dtype: float64
    s.dtype
    Out[9]: dtype('float64')
    s.array
    Out[10]: 
    <PandasArray>
    [ -0.3938514756551117,  -0.9335542253402275,   1.1051972009660536,
       0.7189404297237888, -0.21014576709650493]
    Length: 5, dtype: float64
    s
    Out[11]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    d    0.718940
    e   -0.210146
    dtype: float64

    """
    # series_from_dict()
    # series_from_scalar_value()
    # dataframe_from_dicts_of_series()
    # df_from_dict_of_ndarry_or_list()
    # df_from_structured_or_record_array()
    # df_from_dict()
    # assigning_df()
    # df_alignment_arithmetic()
    bool_df()
