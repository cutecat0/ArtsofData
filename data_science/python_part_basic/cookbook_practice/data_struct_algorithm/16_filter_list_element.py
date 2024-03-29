#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Q: You have a data list, want to get some need value or reduce the length through some rules
    A: Way 1: Simplest way is by the list to get it such as [n for n in data_list if n>0]
       Way 2: Use iterator expression
       Way 3: while rules is too much complex, you can write a special rule function and then put this
              rule function in python inner build filter() function
"""


def get_list_elements():
    # way 1
    lists = [i + 2 for i in range(20)]
    print(lists)
    # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    filtered_list = [n for n in lists if n > 6 and n % 3 == 0]
    print(filtered_list)
    # [9, 12, 15, 18, 21]
    """
        ! way 1 disadvantage: if the input data is very large the output would be large either, 
        which will takes too much storage 
        solution: if you're senstive to storage, I suggest you use iterator strongly! 
    """

    # way 2
    pos = (n for n in lists if n > 6 and n % 3 == 0)
    print(pos)  # <generator object get_list_elements.<locals>.<genexpr> at 0x7fbfe98851d0>
    for i in pos:
        print(i, end='\t')
    # 9	12	15	18	21

    # way 3
    data_list = [0, 1, 6, 8, -6, 'N/A', 'NULL', 's-1', 'None']
    need_list = list(filter(rules, data_list))  # here filter() function creates an iterator, so if you want to get a list, use list() to switch it
    print(need_list)
    # [0, 1, 6, 8, -6, '-1']

    # switch data while filter data
    data_list_2 = [1, 2, 5, 8, 4, -2, -9, -1, 7]
    import math
    print([math.sqrt(x) for x in data_list_2 if x > 0])
    # [1.0, 1.4142135623730951, 2.23606797749979, 2.8284271247461903, 2.0, 2.6457513110645907]

    # for the data that not switch with filter rules, you can't delete it, you use some other value to replace them
    negative_data = [x if x > 0 else 0 for x in data_list_2]
    print(negative_data)
    # [1, 2, 5, 8, 4, 0, 0, 0, 7]

    positive_data = [x if x < 0 else 0 for x in data_list_2]
    print(positive_data)
    # [0, 0, 0, 0, 0, -2, -9, -1, 0]

    # attention !!! itertools.compress()


def rules(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


def filter_v3():
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]

    from itertools import compress

    more5 = [n > 5 for n in counts]
    print(more5)
    #  [False, False, True, False, False, True, True, False]
    result = list(compress(addresses, more5))
    # ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']

    print(result)


if __name__ == '__main__':
    # get_list_elements()

    filter_v3()

