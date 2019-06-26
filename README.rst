A Median Heap in Python
===================================
A simple program to take medians using a heap data structure.


What It Does
------------

- Calculates the median of data in O(1) time.
- Inserting into the data structure takes O(log n) time in the worst case.


Usage
------------
    >>> from MedianHeapPython.medianFinder import MedianFinder
    >>> d1 = 1
    >>> d2 = 2
    >>> d3 = 3
    >>> medianCalculator = MedianFinder()
    >>> medianCalculator.addData(d1)
    >>> medianCalculator.addData(d2)
    >>> medianCalculator.addData(d3)
    >>> print(medianCalculator.getMedian())  # 2
    >>> print()
