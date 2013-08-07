"""Spec"""

import sys
sys.dont_write_bytecode = True

import timeit
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

    def add_method(self, test_method, args=None):
        """Add method to spec"""
        if not test_method:
            raise Exception("No test method")
        if hasattr(test_method, "__call__"):
            test_data = {
                'method_name': test_method.func_name,
                'method_def': test_method,
                'args': args or ()
            }
            self._test_methods.append(test_data)

    def run_specs(self):
        """Run test methods"""
        if not self._test_methods:
            raise Exception("No methods added to suite.")
        for method in self._test_methods:
            args = method.get("args")
            method_def = method.get("method_def")
            method_name = method.get("method_name")
            if args:
                print "Starting timeit on method {0}".format(method_name)
                method_time = timeit.repeat(method_def,
                                            repeat=self.config['repeats'],
                                            number=self.config['count'])
                print "Ended timeit on method {0}".format(method_name)
            else:
                print "Starting timeit on method {0}".format(method_name)
                method_time = timeit.repeat(method_def,
                                            repeat=self.config['repeats'],
                                            number=self.config['count'])
                print "Ended timeit on method {0}".format(method_name)

            self.results[method_name] = (len(method_time) / 
                                         sum(method_time)) *\
                                          self.config['repeats']
