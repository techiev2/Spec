"""Spec"""

import sys
sys.dont_write_bytecode = True

import timeit
from collections import OrderedDict
# from profile import Profile


class Spec(object):
    """Spec class"""
    def __init__(self, config=None):
        """Spec class init"""
        default_config = {
            'repeats': 100,
            'calls': 100
        }
        config_keys = ('repeats', 'calls')
        if not (config or isinstance(config, dict)):
            config = default_config
        else:
            config = { x : config[x] for x in config if x in config_keys}
            if not config:
                config = default_config

        self._test_methods = []
        self.config = config
        self.results = {}

    def clear_specs(self):
        """Clear existing test specs"""
        self._test_methods, self.results = [], {}

    def call_timeit(self, method):
        """Helper to call timeit on method and add to results"""
        if not (method and hasattr(method.get("method_def", {}), "__call__")):
            raise Exception("Not a method")
        args = method.get("args")
        method_def = method.get("method_def")
        method_name = method.get("method_name")
        if args:
            print "Starting timeit on method {0}".format(method_name)
            timer = timeit.Timer(lambda: method_def.__call__(*args))
            method_time = timer.repeat(repeat=self.config['repeats'],
                                       number=self.config['calls'])
            print "Ended timeit on method {0}".format(method_name)
        else:
            print "Starting timeit on method {0}".format(method_name)
            method_time = timeit.repeat(method_def,
                                        repeat=self.config['repeats'],
                                        number=self.config['calls'])
            print "Ended timeit on method {0}".format(method_name)

        if not self.results.get(method_name):
            self.results[method_name] = {
                "timeit": (len(method_time) /\
                            sum(method_time)) *\
                              self.config['repeats']
            }
        else:
            self.results[method_name]['timeit'] = (len(method_time)\
                                                    / sum(method_time)) *\
                                                    self.config['repeats']
        if self.config.get("sort"):
            self.results = OrderedDict(sorted(self.results.keys(),
                                              key=lambda x: x[1]))

    def add_method(self, test_method, args=None):
        """Add method to spec"""
        if not test_method:
            raise Exception("No test method")
        if hasattr(test_method, "__call__"):
            method_name = test_method.func_name
            if method_name == '<lambda>':
                # Attempted fix to uniquely identify lambdas
                method_name = "{0}_{1}".format(
                                method_name,
                                [x.get('method_name')\
                                 for x in\
                                  self._test_methods].count('<lambda>'))
            test_data = {
                'method_name': method_name,
                'method_def': test_method,
                'args': args or ()
            }
            self._test_methods.append(test_data)

    def run_specs(self):
        """Run test methods"""
        if not self._test_methods:
            raise Exception("No methods added to suite.")
        for method in self._test_methods:
            self.call_timeit(method)
