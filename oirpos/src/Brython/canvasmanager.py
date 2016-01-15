#!/usr/bin/python

from browser import alert

# Class responsible for drawing function on canvas.
class CanvasManager:

	def __init__(self, v, p):
		self.v = v
		self.p = p

	# Draws function on given canvas.
	def drawFunction(self, ctx):
		step = self.v.unitsPerTick / self.v.getSpacing()
		xList = self.computeX(step)
		yList = self.computeY(xList)
		self.addDataSet(ctx, self.v.fcolor, xList, yList, step)
	
	# Computes list of X-values for current plot.
	def computeX(self, step):
		w = self.v.canvasWidth
		half = int(w/2)
		
		xList = []
		i = 0
		valPositive = 0
		valNegative = 0
		xList.append(0)
		while i < half:
			valPositive += step
			valNegative -= step
			xList.append(valPositive)
			xList.append(valNegative)
			i = i+1
		xList.sort()
		xList.pop()
		return xList
	
	# Computes list of Y-values for current plot.
	def computeY(self, xlist):
		h = self.v.canvasHeight
		ylist = []
		for item in xlist:
			y = self.p.fetch(item)
			ylist.append(y)
		return ylist

	# Draws set of points on given canvas.
	def addDataSet(self, ctx, color, xs, ys, step):
		w = self.v.canvasWidth
		half = int(w/2)
		h = self.v.canvasHeight
		
		ctx.beginPath()
		ctx.strokeStyle = color
		ctx.lineWidth = 1

		pointCacheX = int(xs[0]/step)+half 
		pointCacheY = self.convertYToWorkspace(ys[0], step)
		for i in range(1, len(xs)):
			x = (xs[i]/step)+half
			y = self.convertYToWorkspace(ys[i], step) 
			if (y >= 0 and y<h and pointCacheY >= 0 and pointCacheY<h):
				ctx.moveTo(pointCacheX, pointCacheY)
				ctx.lineTo(x, y)
				ctx.stroke()
			pointCacheX = x
			pointCacheY = y

	# Converts computed Y to proper y-position on the screen.
	def convertYToWorkspace(self, y, step):
		h = self.v.canvasHeight
		newY = (y/step)
		newY = newY*(-1)
		newY += (h/2)
		return int(newY)

