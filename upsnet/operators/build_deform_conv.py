# ---------------------------------------------------------------------------
# Unified Panoptic Segmentation Network
#
# Copyright (c) 2018-2019 Uber Technologies, Inc.
#
# Licensed under the Uber Non-Commercial License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at the root directory of this project. 
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Written by Yuwen Xiong
# ---------------------------------------------------------------------------
import torch
import os
from functools import reduce
# from itertools import accumulate
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
from subprocess import call

def accumulate(iterable, func, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def _create_module_dir(base_path, fullname):
    module, _, name = fullname.rpartition('.')
    if not module:
        target_dir = name
    else:
        target_dir = reduce(os.path.join, fullname.split('.'))
    target_dir = os.path.join(base_path, target_dir)
    try:
        os.makedirs(target_dir)
    except os.error:
        pass
    for dirname in accumulate(fullname.split('.'), os.path.join):
        init_file = os.path.join(base_path, dirname, '__init__.py')
        open(init_file, 'a').close()  # Create file if it doesn't exist yet
    return name, target_dir

base_path = os.path.abspath(os.path.dirname('.'))
_create_module_dir(base_path, '_ext.deform_conv')

setup(
    name='deform_conv',
    ext_modules=[
        CUDAExtension('deform_conv_cuda', [
            'src/deform_conv_cuda.cpp',
            'src/deform_conv_kernel.cu',],
            include_dirs=[os.path.join(base_path, 'src')],
            extra_compile_args={
                'cxx': [],
                'nvcc': ['-O2']}
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)

call('mv deform_conv_cuda*.so _ext/deform_conv/', shell=True)
