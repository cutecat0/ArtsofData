#! usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
from itertools import groupby

"""
    Q: YOU have the list of one dict or object, and you want to iterator access it with a pointed parameter?
    A:  itertools.groupby() function can solve this problem quickly
"""


def group_record_by_one_pointed_parameter():
    """
    now, suppose you want to iterator the above record through 'date' parameter
    firstly, you need to order by the record through the pointed parameter which is 'date'
    then, you can call itertools.groupby() function
    """
    # suppose you already have the follow records:
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    # sort by the desired field first
    rows.sort(key=itemgetter('date'))

    # iterator in groups
    for date, item in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in item:
            print(' ', i)

    # result:
    """
    07/01/2012
    {'address': '5412 N CLARK', 'date': '07/01/2012'}
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
    07/02/2012
    {'address': '5800 E 58TH', 'date': '07/02/2012'}
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
    {'address': '1060 W ADDISON', 'date': '07/02/2012'}
    07/03/2012
    {'address': '2122 N CLARK', 'date': '07/03/2012'}
    07/04/2012
    {'address': '5148 N CLARK', 'date': '07/04/2012'}
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
    """


def chatGPT_way():
    # Sample data
    records = [
        {'name': 'Alice', 'age': 25, 'gender': 'Female'},
        {'name': 'Bob', 'age': 30, 'gender': 'Male'},
        {'name': 'Charlie', 'age': 35, 'gender': 'Male'},
        {'name': 'David', 'age': 40, 'gender': 'Male'},
        {'name': 'Emma', 'age': 45, 'gender': 'Female'},
        {'name': 'Frank', 'age': 50, 'gender': 'Male'}
    ]

    # Group by gender
    groups = {}
    for record in records:
        key = record['gender']
        if key not in groups:
            groups[key] = []
        groups[key].append(record)

    # Print the groups
    for key, group in groups.items():
        print(f"{key}: {group}")

    # result:
    """
    Female: [{'name': 'Alice', 'age': 25, 'gender': 'Female'}, {'name': 'Emma', 'age': 45, 'gender': 'Female'}]
    Male: [{'name': 'Bob', 'age': 30, 'gender': 'Male'}, {'name': 'Charlie', 'age': 35, 'gender': 'Male'}, {'name': 'David', 'age': 40, 'gender': 'Male'}, {'name': 'Frank', 'age': 50, 'gender': 'Male'}]
    """


def chatGPT_way2():
    import itertools

    # Sample data
    records = [
        {'name': 'Alice', 'age': 25, 'gender': 'Female'},
        {'name': 'Bob', 'age': 30, 'gender': 'Male'},
        {'name': 'Charlie', 'age': 35, 'gender': 'Male'},
        {'name': 'David', 'age': 40, 'gender': 'Male'},
        {'name': 'Emma', 'age': 45, 'gender': 'Female'},
        {'name': 'Frank', 'age': 50, 'gender': 'Male'}
    ]

    # Sort by gender
    records.sort(key=lambda x: x['gender'])

    # Group by gender
    groups = {}
    for key, group in itertools.groupby(records, key=lambda x: x['gender']):
        groups[key] = list(group)

    # Print the groups
    for key, group in groups.items():
        print(f"{key}: {group}")

    # result
    """
    Female: [{'name': 'Alice', 'age': 25, 'gender': 'Female'}, {'name': 'Emma', 'age': 45, 'gender': 'Female'}]
    Male: [{'name': 'Bob', 'age': 30, 'gender': 'Male'}, {'name': 'Charlie', 'age': 35, 'gender': 'Male'}, {'name': 'David', 'age': 40, 'gender': 'Male'}, {'name': 'Frank', 'age': 50, 'gender': 'Male'}]
    """


if __name__ == '__main__':
    group_record_by_one_pointed_parameter()
    chatGPT_way()
    chatGPT_way2()