# -*- coding: utf-8 -*-
import importlib
import sys
import time

_modules = set()


class ImportHookFinder:

    def find_module(self, fullname, path=None):
        print(fullname + '  find_module')
        if 'hello' in fullname:
            return self

    def load_module(self, fullname):
        print(fullname + '  load_module')
        if fullname in sys.modules:
            return sys.modules[fullname]

        sys.meta_path.pop(0)
        try:
            module = importlib.import_module(fullname)
        except ImportError:
            return

        wrap_module(fullname, module)

        sys.modules[fullname] = module
        sys.meta_path.insert(0, self)
        return module


def init():
    # sys.meta_path.append(ImportHookFinder())
    sys.meta_path.insert(0, ImportHookFinder())


def wrap_module(fullname, module):
    print('wrap_module')
    if 'hello' in fullname:
        module.hello2 = FuncWrapper(module.hello2)


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
        spent = self.end_time - self.start_time
        print('{0}.{1} spent {2} s'.format(
            self.func.__module__, self.func.__name__, spent
        ))
