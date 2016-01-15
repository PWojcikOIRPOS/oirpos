#!/usr/bin/python

from browser import document as doc
from browser import alert

# Class responsible for validating parameters related to canvas' dimensions.
# Author: Paweł Wójcik
class PlotParamValidator:

	SPACING = 30.0 # tick spacing

	# Method checks whether given text is not empty.
	def isNotEmpty(self, txt):
		if txt and txt.strip():
			return True
		return False
			
	# Returns information about validation.
	def isValid(self):
		return self.valid

	def __init__(self):
		fcolor = doc["fcolor"].value
		pertickStr = doc["pertick"].value
		canvasWidthStr = doc["canvaswidth"].value
		canvasHeightStr = doc["canvasheight"].value
		self.valid = self.isNotEmpty(canvasWidthStr) and self.isNotEmpty(canvasHeightStr) and self.isNotEmpty(fcolor) \
				and self.isNotEmpty(pertickStr)
		if self.isValid():
			self.fcolor = fcolor
			self.unitsPerTick = int(pertickStr)
			self.canvasWidth = int(canvasWidthStr)
			self.canvasHeight = int(canvasHeightStr)
			self.xAxis = self.canvasHeight / 2 
			self.yAxis = self.canvasWidth / 2
		
			pertickForm = doc["pertick"]
			widthForm = doc["canvaswidth"]
			heightForm = doc["canvasheight"]
			pertickForm.disabled = "disabled"
			widthForm.disabled = "disabled"
			heightForm.disabled = "disabled"

	# Method shows information about invalid input.
	def block(self):
		alert("All required parameters are not filled!")

	def getSpacing(self):
		return PlotParamValidator.SPACING
