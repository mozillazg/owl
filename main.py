# -*- coding: utf-8 -*-
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))


def main():
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    os.environ['PYTHONPATH'] = '{}:{}'.format(
        os.path.join(current_dir, 'bootstrap'),
        os.environ.get('PYTHONPATH')
    )
    os.execl(sys.executable, sys.executable, *args)

if __name__ == '__main__':
    main()
