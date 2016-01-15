#!/usr/bin/python

from browser import document as doc
from browser import html
from browser import alert
from canvasmanager import CanvasManager
import math

# Class responsible for plotting polynomial functions.
# Author: Paweł Wójcik
class Plot:

	def __init__(self, v, parser):
		self.v = v
		self.p = parser
		self.mgr = CanvasManager(v, parser)

	# Starts plotting.
	def run(self):
		container = doc['container']
		container.clear()
		self.step = self.v.unitsPerTick / self.v.getSpacing()
		canvas = self.drawCanvas()
		ctx = canvas.getContext('2d')
		self.drawAxis(ctx)
		self.mgr.drawFunction(ctx)	
		container <= canvas

	# Creates HTML5 canvas with drawn axes, ticks and function.
	def drawCanvas(self):
		w = self.v.canvasWidth
		h = self.v.canvasHeight
		canvas = html.CANVAS(width = w, height = h, id = "brythoncanvas")
		ctx = canvas.getContext('2d')
		ctx.fillStyle = "#131313"
		ctx.fillRect(0, 0, w, h)
		return canvas	
	
	# Draws X and Y axes
	def drawAxis(self, ctx):
		ctx.beginPath()
		ctx.strokeStyle = "white"
		ctx.lineWidth = 2
		ctx.moveTo(0, self.v.xAxis)
		ctx.lineTo(self.v.canvasWidth, self.v.xAxis)
		ctx.stroke()
		ctx.moveTo(self.v.yAxis, 0)
		ctx.lineTo(self.v.yAxis, self.v.canvasHeight)
		ctx.stroke()
		self.drawUnits(ctx)

	# Draws ticks with labels
	def drawUnits(self,ctx):
		self.drawTicksHorizontal(ctx)
		self.drawTicksVertical(ctx)
	
	# Draws horizontal ticks with labels
	def drawTicksHorizontal(self, ctx):
		halfW =	self.v.canvasWidth / 2	
		ticksCount = (halfW / self.v.getSpacing()) 
		for i in range(1, ticksCount+1):
			ctx.beginPath()
			ctx.strokeStyle = "white"
			ctx.lineWidth = 2
			x = self.v.yAxis + (i*self.v.getSpacing())
			ctx.moveTo(x, self.v.xAxis-4)
			ctx.lineTo(x, self.v.xAxis+4)
			ctx.stroke()
			negX = self.v.yAxis - (i*self.v.getSpacing())
			ctx.moveTo(negX, self.v.xAxis-4)
			ctx.lineTo(negX, self.v.xAxis+4)
			ctx.stroke()
			xForLabel = i*self.v.unitsPerTick
			xForLabelNeg = i*(-1)*self.v.unitsPerTick
			self.drawLabelOnX(ctx, x, xForLabel)
			self.drawLabelOnX(ctx, negX, xForLabelNeg)

	# Draws single label on X-axis
	def drawLabelOnX(self, ctx, x, xlabel):
		ctx.fillStyle = "white"
		ctx.font = "8px Arial"
		label = str(int(xlabel))
		ctx.fillText(label, x-2, self.v.xAxis+10)
	
	# Draws vertical ticks with labels
	def drawTicksVertical(self, ctx):
		halfH =	self.v.canvasHeight / 2	
		ticksCount = (halfH / self.v.getSpacing()) 
		for i in range(1, ticksCount+1):
			ctx.beginPath()
			ctx.strokeStyle = "white"
			ctx.lineWidth = 2
			y = self.v.xAxis + (i*self.v.getSpacing())
			ctx.moveTo(self.v.yAxis-4, y)
			ctx.lineTo(self.v.yAxis+4, y)
			ctx.stroke()
			negY = self.v.xAxis - (i*self.v.getSpacing())
			ctx.moveTo(self.v.yAxis-4, negY)
			ctx.lineTo(self.v.yAxis+4, negY)
			ctx.stroke()
			yForLabel = i*self.v.unitsPerTick
			yForLabelNeg = i*(-1)*self.v.unitsPerTick
			self.drawLabelOnY(ctx,y, yForLabel)
			self.drawLabelOnY(ctx,negY, yForLabelNeg)

	# Draws single label on Y-axis
	def drawLabelOnY(self, ctx, y, yLabel):
		ctx.fillStyle = "white"
		ctx.font = "8px Arial"
		label = str(int((-1)*(yLabel)))
		ctx.fillText(label, self.v.yAxis+10, y)

