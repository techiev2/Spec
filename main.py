"""
Spec main
Created on 06-Aug-2013
"""
# coding=utf-8
__author__ = "Sriram Velamur"


import sys
sys.dont_write_bytecode = True
from Spec import Spec


def x():
    a = False
    if a:
        return 1
    else:
        return 2

def y():
    a = None
    if a:
        return 1
    else:
        return 2


def ranger(min_val=None, max_val=None):
    if not (min_val and max_val):
        min_val, max_val = 1, 1000
    z = 0
    for x in range(min_val, max_val):
        z += 1
    return z


def xranger(min_val=None, max_val=None):
    if not (min_val and max_val):
        min_val, max_val = 1, 1000
    z = 0
    for x in range(min_val, max_val):
        z += 1
    return z


if __name__ == "__main__":
    s = Spec({
        'repeats': 10,
        'calls': 10,
        'sort': True
    })
    s.add_method(ranger, (1, 10000))
    s.add_method(xranger, (1, 10000))
    s.run_specs()
    print s.results
    s.clear_specs()
    s.add_method(x)
    s.add_method(y)
    s.run_specs()
    print s.results
