import os
import sys


def fix_path():
    base, a = os.path.split(os.path.dirname(__file__))
    sys.path.append(base)
    sys.path.append(os.path.join(base, 'lib'))

fix_path()
