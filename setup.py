#!/usr/bin/env python

# python distutils.core.setup reference at
# "https://docs.python.org/2/distutils/apiref.html"
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

# install data_files with the source
for scheme in list(INSTALL_SCHEMES.values()):
    scheme['data'] = scheme['purelib']

setup(name='NuGridpy',
    version='0.1.6401', 
    description='Python tools for NuGrid',
    long_description=open('README', 'r').read(), # get discription from README
    author='NuGrid Team',
    author_email='samuel.jones@h-its.org',
    url='http://www.nugridstars.org/',
    #download_url='http://www.nugridstars.org/', #must be uptodate if used
    #py_modules=['ppn', 'ppm', 'nugridse', 'mesa', 'data_plot', 'utils',
    #            'ascii_table', 'h5T','grain'],
    py_modules=['ppn', 'nugridse', 'mesa', 'data_plot', 'utils',
                'ascii_table', 'h5T','grain','astronomy'],
    # https://pypi.python.org/pypi?:action=list_classifiers : PyPI classifiers.
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console', 'Framework :: IPython',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering :: Astronomy',
                 'Topic :: Scientific/Engineering :: Visualization'],
    license='BSD 3-clause',
    platforms=['Linux', 'Windows', 'OS X'],
    data_files=[('./NuGridpy', ['LICENSE', 'README', 'AUTHORS'])])
