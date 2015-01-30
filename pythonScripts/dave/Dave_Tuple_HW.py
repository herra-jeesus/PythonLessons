#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

listOfCrosses = []

print '\nEnter field dimensions in format x,y'
fieldDimensions = tuple(map(int,raw_input().split(',')))
print "\nField size is: %s" % (fieldDimensions,)

fieldWidth 	= 	fieldDimensions[1]
fieldHeight = 	fieldDimensions[0]

while True:
	i = raw_input("\nNow enter cross locations in format x,y then Enter (or type 'done' then Enter to display field): ")
	if i == "done":
		break
	crossLocation = tuple(map(int,i.split(',')))
	print "\nYou placed a cross at location: %s" % (crossLocation,)

	if crossLocation[0]<=fieldHeight and crossLocation[1]<=fieldWidth and crossLocation[0]>0 and crossLocation[1]>0:
		if crossLocation not in listOfCrosses:
			listOfCrosses.append(crossLocation)
	else:
		print "--> Error: cross outside the field dimensions: %s - try again!\n" % (fieldDimensions,)

def displayCrosses(fieldDimensions,listOfCrosses):
	display = numpy.zeros((fieldWidth,fieldHeight))

	for cross in listOfCrosses:

		xCoord = cross[1]-1
		yCoord = cross[0]-1

		display [xCoord,yCoord] = -1

		for y in range(-1,2):
			for x in range(-1,2):

				if xCoord+x>=0 and yCoord+y>=0 and xCoord+x<fieldWidth and yCoord+y<fieldHeight and not(x==y==0):
					
					#print '\nIncrementing value in position: ',[yCoord+y+1,xCoord+x+1]

					tupleToTest = (yCoord+y+1,xCoord+x+1)
					if tupleToTest not in listOfCrosses: #Prevents 'crosses' (minus 1 elements) from being incremented
	    				
						display [xCoord+x,yCoord+y] += 1
	print "\n"
	print display
	print "\n"

displayCrosses(fieldDimensions,listOfCrosses)