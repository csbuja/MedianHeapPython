from heapq import heapify, heappush, heappop

class MedianFinder(object):
	def __init__(self, x, y):
		self.minHeap = []
		heapify(self.minHeap)
		self.maxHeap = []
		heapify(self.maxHeap)

		if x < y:
			self.pushMax(x)
			self.pushMin(y)
		else:
			self.pushMax(y)
			self.pushMin(x)
	def pushMax(self, val):
		heappush(self.maxHeap, float(-1 * val))
	def pushMin(self,val):
		heappush(self.minHeap, float(val) )
	def topMax(self):
		return -1 * self.maxHeap[0]
	def topMin(self):
		return self.minHeap[0]
	def popMin(self):
		x = self.topMin()
		heappop(self.minHeap)
		return x 
	def popMax(self):
		x = self.topMax()
		heappop(self.maxHeap)
		return x
	def addData(self, x): #assumes x is an integer
		if x < self.topMax():
			self.pushMax(x)
		else:
			self.pushMin(x)
		#balance!
		if len(self.maxHeap) > len(self.minHeap):
			y = self.popMax()
			self.pushMin(y)
		if len(self.minHeap ) > len(self.maxHeap):
			y = self.popMin()
			self.pushMax(y)
	def getMedian(self):
		if len(self.maxHeap) > len(self.minHeap):
			return self.topMax()
		elif len(self.minHeap ) > len(self.maxHeap):
			return self.topMin()
		else:
			return (self.topMax() + self.topMin() )/2

m = MedianFinder(1,2)
m.addData(4)
m.addData(4)
print m.getMedian()
