# -*- coding: utf-8 -*-
import importlib
import sys
import time


class ImportHookFinder:

    def find_module(self, fullname, path=None):
        print(fullname + '  find_module')
        return self

    def load_module(self, fullname):
        print(fullname + '  load_module')
        if fullname in sys.modules:
            return sys.modules[fullname]

        finder = sys.meta_path.pop()
        module = importlib.import_module(fullname)

        wrap_module(fullname, module)

        sys.modules[fullname] = module
        sys.meta_path.append(finder)
        return module

sys.meta_path.append(ImportHookFinder())


def wrap_module(fullname, module):
    if 'hello' in fullname:
        module.hello = FuncWrapper(module.hello)


class FuncWrapper:

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self

    def __call__(self, *args, **kwargs):
        with Timer(self.func):
            return self.func(*args, **kwargs)


class Timer:

    def __init__(self, func):
        self.func = func

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        spend = self.end_time - self.start_time
        print('{0} spend {1} s'.format(self.func.__name__, spend))
