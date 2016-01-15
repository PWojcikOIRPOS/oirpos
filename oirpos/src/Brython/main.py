#!/usr/bin/python

from browser import document as doc
from browser import html
from browser import alert
from validator import PlotParamValidator
from parser import FunctionParser
from plot import Plot
from canvasmanager import CanvasManager 

# Main class for plotting.
# Plotting is evaluated when button with ID="redraw" is clicked.

def onclickmethod(*args):
	canvasExists = True
	try:
		canvas = doc['brythoncanvas']
	except KeyError:
		canvasExists = False

	v = PlotParamValidator()
	if v.isValid():
		pr = FunctionParser()	
		if pr.canParse():
			if (canvasExists == True):
				ctx = canvas.getContext('2d')
				mgr = CanvasManager(v, pr)
				mgr.drawFunction(ctx)
			else:
				p = Plot(v, pr)
				p.run()
		else:
			pr.block()
	else:
		v.block()
		
# Button binding
doc["redraw"].bind("click", onclickmethod)
