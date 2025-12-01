"""
Spec main
Created on 06-Aug-2013
"""
# coding=utf-8
__author__ = "Sriram Velamur"


import sys
sys.dont_write_bytecode = True
from Spec import Spec

def as_list_comprehension(data):
    return [_*2 for _ in data]


def as_map_inner_fn(data):
    def square_(num):
        return num * 2
    return list(map(square_, data))


def square(num):
    return num * 2


def as_map_external_fn(data):
    return list(map(square, data))


def imperative(data):
    results = []
    for item in data:
        results.append(item * 2)
    return results


if __name__ == "__main__":
    s = Spec({
        'repeats': 1000,
        'calls': 1000,
        'sort': True,
     	'timeit': True
    })
    source_data = (1, 10000)
    s.add_method(as_list_comprehension, (source_data,))
    s.add_method(as_map_inner_fn,(source_data,))
    s.add_method(as_map_external_fn,(source_data,))
    s.add_method(imperative,(source_data,))
    s.run_specs()
    print(s.output_str)
    s.clear_specs()
