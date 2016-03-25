#!/usr/bin/env python

import sys
import os.path

try:
   from setuptools import setup, Extension
except ImportError:   
   sys.stderr.write( "Could not import 'setuptools', falling back to 'distutils'.\n" )
   from distutils.core import setup, Extension

if sys.version_info[0] < 2 or sys.version_info < 5:
   sys.stderr.write( "Error in setup script for MixedHTSeq:\n" )
   sys.stderr.write( "You need at least version 2.5 of Python to use MixedHTSeq.\n" )
   sys.exit( 1 )

if sys.version_info[0] >= 3:
   sys.stderr.write( "Error in setup script for MixedHTSeq:\n" )
   sys.stderr.write( "Sorry, this package does not yet work with Python 3.\n" )
   sys.stderr.write( "Please use Python 2.x, x>=5.\n" )
   sys.exit( 1 )

try:
   import numpy
except ImportError:
   sys.stderr.write( "Setup script for MixedHTSeq: Failed to import 'numpy'.\n" )
   sys.stderr.write( "Please install numpy and then try again to install MixedHTSeq.\n" )
   sys.exit( 1 )
   
numpy_include_dir = os.path.join( os.path.dirname( numpy.__file__ ), 'core', 'include' )
 

setup( name = 'MixedHTSeq',
       version = file("VERSION").readline().rstrip(),
       author = 'Simon Anders',
       author_email = 'sanders@fs.tum.de',
       url = 'http://www-huber.embl.de/users/anders/HTSeq/',
       description = "A framework to process and analyze data from " +
          "high-throughput sequencing (HTS) assays",
       classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX',
          'Programming Language :: Python'
       ],
       requires = [ 'numpy', 'python (>=2.5, <3.0)' ],
       
       py_modules = [ 
          'MixedHTSeq._HTSeq_internal', 
          'MixedHTSeq.StepVector',
          'MixedHTSeq._version',
          #'MixedHTSeq.scripts.qa',
          #'MixedHTSeq.scripts.count'
       ],
       ext_modules = [ 
          Extension( 'MixedHTSeq._HTSeq', 
             ['src/_HTSeq.c'], include_dirs=[numpy_include_dir], extra_compile_args=['-w'] ),
          Extension( 'MixedHTSeq._StepVector', 
             ['src/StepVector_wrap.cxx'], extra_compile_args=['-w'] ),
       ],
       scripts = [
          #'scripts/htseq-qa',
          #'scripts/htseq-count',
       ]
     )


