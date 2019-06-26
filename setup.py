from setuptools import setup


def contentsOfReadMe():
    with open('README.rst') as f:
        return f.read()


setup(
    name='MedianHeapPython',
    version='1.0.6',
    packages=["MedianHeapPython"],
    description='Calculates the median of a data stream in O(log n) time using a heap!',
    long_description=contentsOfReadMe(),
    author='Spencer Buja',
    author_email='csbuja@umich.edu',
    url='https://github.com/csbuja/MedianHeapPython',
    license='MIT',
    platforms='ALL'
)
