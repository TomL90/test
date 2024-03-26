from setuptools import setup

import sys
if sys.version_info < (2,7):
    sys.exit('Sorry, Python < 2.7 is not supported')

setup(
    name='my_module',
    version='0.1.0',    
    description='A example Python package',
    url='',
    author='Tommaso Lari',
    author_email='123.gmail',
    license='free',
    packages=['my_module'],
    install_requires=[
                      'numpy', 'scipy'                    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)