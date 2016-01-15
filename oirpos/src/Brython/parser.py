#!/usr/bin/python

from browser import document as doc
import math

# Class responsible for parsing input parameters related to plotted function.
# Author: Paweł Wójcik
class FunctionParser:
	
	# Method parses proper HTML forms to internal variables.
	def parse(self):
		self.x1 = float(doc["functionx1"].value)
		self.x2 = float(doc["functionx2"].value)
		self.x3 = float(doc["functionx3"].value)
		self.d = float(doc["functiond"].value)
		return (self.x1 != 0.0) or (self.x2 != 0.0) or (self.x3 != 0.0)

	def __init__(self):
		self.valid = self.parse()

	# Method returns information whether given function is valid.
	def canParse(self):
		return self.valid

	# Method returns f(x) value for given 'x'.
	def fetch(self, x):
		return math.pow(x,3)*self.x3 + math.pow(x,2)*self.x2 + x*self.x1 + self.d
	
	# Shows information about invalid function.
	def block(self):
		alert("Function cannot be parsed.")
