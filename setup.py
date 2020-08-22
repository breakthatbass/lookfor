from setuptools import setup, find_packages

setup(
    name='lookfor',
    version='1.0.0',
    description='terminal program to look for things',
    author='Taylor Gamache',
    author_email='gamache.taylor@gmail.com',
    url='https://github.com/breakthatbass/lookfor',
    packages=find_packages(),
    license='MIT',
    entry_points={
        'console_scripts' : ['lookfor = lookfor.__main__:main']
   }
)