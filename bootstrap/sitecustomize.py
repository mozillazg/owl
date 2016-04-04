# -*- coding: utf-8 -*-
# import importlib
# import importlib.machinery
# import importlib.util
# import os
# import sys

import ext

# paths = sys.path
# current_dir = os.path.dirname(os.path.realpath(__file__))
#
# if current_dir in paths:
#     paths.remove(current_dir)
#
# # 导入其他模块中定义的 sitecustomize
# spec = importlib.machinery.PathFinder.find_spec('sitecustomize', sys.path)
# if spec is not None:
#     importlib.util.module_from_spec(spec)


ext.init()
