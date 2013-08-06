"""
Spec main
Created on 06-Aug-2013
"""
# coding=utf-8
__author__ = "Sriram Velamur"


import sys
sys.dont_write_bytecode = True
from Spec import Spec


def test():
    """Rand"""
    print "x"


if __name__ == "__main__":
    s = Spec({
            'repeats': 10
        })
    s.add_method(test)
    s.run_specs()
