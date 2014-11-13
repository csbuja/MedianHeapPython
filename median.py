from heapq import heapify, heappush, heappop

class MedianFinder(object):
	def __init__(self):
		self.minHeap = []
		heapify(self.minHeap)
		self.maxHeap = []
		heapify(self.maxHeap)
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
		if not (len(self.maxHeap) or len(self.minHeap)):
			self.pushMax(x)
		elif len(self.maxHeap) == 1 and not len(self.minHeap) :
			if x > self.topMax():
				self.pushMin(x)
			else:
				y = self.popMax()
				self.pushMax(x)
				self.pushMin(y)
		else:
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
	def getMedian(self): # returns None if no data has been given to the median finder
		if len(self.maxHeap)==0 and len(self.minHeap)==0:
			return
		if len(self.maxHeap) > len(self.minHeap):
			return self.topMax()
		elif len(self.minHeap ) > len(self.maxHeap):
			return self.topMin()
		else:
			return (self.topMax() + self.topMin() )/2
