from MedianHeapPython.medianFinder import MedianFinder

###
# Example 1.
# Odd Number of cases.
###
print("Odd # of examples")

print([1, 2, 3])

d1 = 1
d2 = 2
d3 = 3

medianCalculator = MedianFinder()
medianCalculator.addData(d1)
medianCalculator.addData(d2)
medianCalculator.addData(d3)

print(medianCalculator.getMedian())  # returns the median very efficiently
print()

###
# Example 2.
# Even number of cases
###
print("Even # of examples")
print([1, 2, 3, 2])

d1 = 1
d2 = 2
d3 = 3

medianCalculator = MedianFinder()
medianCalculator.addData(d1)
medianCalculator.addData(d2)
medianCalculator.addData(d3)
medianCalculator.addData(d2)

print(medianCalculator.getMedian())
print()

###
# Example 3.
# Large number of examples
###
print("Even, large # of examples")
print("[1,...,100,1,...,100]")

dataList = [x + 1 for x in range(100)] + [x + 1 for x in range(100)]

medianCalculator = MedianFinder()

[medianCalculator.addData(data) for data in dataList]

# Answer should 50.5
print(medianCalculator.getMedian())
print()
