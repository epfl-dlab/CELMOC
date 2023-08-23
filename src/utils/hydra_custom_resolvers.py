import math
import os

from omegaconf import OmegaConf


def add_args(*args):
    return sum(float(x) for x in args)


def add_args_int(*args):
    return int(sum(float(x) for x in args))


def multiply_args(*args):
    return math.prod(float(x) for x in args)


def multiply_args_int(*args):
    return int(math.prod(float(x) for x in args))


def floor_division(dividend, divisor):
    return dividend // divisor


def num_dir_in_directory(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        return 0

    is_dir = os.path.isdir(path)
    if not is_dir:
        raise Exception(f"Path `{path}` does not correspond to a directory!")

    ls_dir = [fp for fp in os.listdir(path) if os.path.isdir(os.path.join(path, fp))]
    return len(ls_dir)


def path_to_python_executable():
    import sys

    return sys.executable


def max_args(*args):
    return max(x for x in args)


OmegaConf.register_new_resolver("add", add_args)
OmegaConf.register_new_resolver("mult", multiply_args)

OmegaConf.register_new_resolver("add_int", add_args_int)
OmegaConf.register_new_resolver("mult_int", multiply_args_int)

OmegaConf.register_new_resolver("num_dir", num_dir_in_directory)

OmegaConf.register_new_resolver("path_to_python_executable", path_to_python_executable)
OmegaConf.register_new_resolver("floor_div", floor_division)

OmegaConf.register_new_resolver("max", max_args)
