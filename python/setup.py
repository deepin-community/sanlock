# Copyright 2010-2019 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions
# of the GNU General Public License v.2.

from setuptools import setup, Extension

sanlocklib = ['sanlock']
sanlock = Extension(name='sanlock',
                    sources=['sanlock.c'],
                    include_dirs=['../src'],
                    library_dirs=['../src'],
                    extra_compile_args=["-std=c99"],
                    libraries=sanlocklib)

version = None
with open('../VERSION') as f:
    version = f.readline()

setup(name='sanlock-python',
      version=version,
      description='Python bindings for the sanlock library',
      ext_modules=[sanlock])
