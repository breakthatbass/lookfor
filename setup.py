from setuptools import setup, find_packages

setup(
    name='lookfor',
    version='1.0.0',
    author='Taylor Gamache',
    entry_points={
        'console_scripts' : ['lookfor = lookfor.lookfor:main']
   }
)