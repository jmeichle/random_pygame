#!/usr/bin/python

import pygame, time, sys, random, math
from pprint import pprint
w = 600                 #set width of screen
h = 500                 #set height
offset = 250   
lineColor = (255, 255, 255)  

debugOne = False

if len(sys.argv) >= 2:
	numDimensions = int(sys.argv[1])
else:
	print "Number of dimensions is arg 1. exiting."
	sys.exit(1)
if len(sys.argv) == 3:
	debugOne = True

sideLengthMax = 120
lineThickness = 1
offset = 300

# Utility function to no tgenerate angles within 60 degrees of each other (yea this will be a problem if going more than 5-6 D)
pastAngles = []
def getRandomAngle():
	while True:
		newAngle = int((random.random() * 360 ))
		if not len(pastAngles) == 0:
			isGood = True;
			for angle in pastAngles:
				if not ( newAngle > angle-30 and newAngle < angle+30 ):
					pass # totally a good potential angle. need to iterate rest of list tho.
				else:
					isGood = False 
			if isGood:
				pastAngles.append(newAngle)
				return newAngle
			else:
				pass
		else:
			pastAngles.append(newAngle)
			return newAngle

# set offset
def getPointWithOffset(pt):
	return (pt[0] + offset, pt[1] + offset)
def toRadians(degrees):
	return degrees * ((2 * math.pi) / 360)

pts = [ (0,0) ]
lines = []

for dim in range(numDimensions):
	newpts = []
	newlines = []
	numOrigPts = len(pts)
	randomAngle = getRandomAngle()
	randomLength = int(( random.random() * sideLengthMax ))
	if randomLength < 40:
		randomLength = randomLength + 40
	xadd = int(math.cos(toRadians(randomAngle)) * randomLength)
	yadd = int(math.sin(toRadians(randomAngle)) * randomLength)
	for idx,pttuple in enumerate(pts):
		# yay 1 easy line to calc all new points for higher D
		newpts.append ( ( pttuple[0] + xadd, pttuple[1] + yadd  ) )
		# connect prev D to new D
		newlines.append ( ( idx, (numOrigPts + idx) ) )
	# need to go and add lines from old D in the new D
	for line in lines:
		newlines.append ( ( ( line[0] + numOrigPts ), ( line[1] + numOrigPts ) ) )
	pts = pts + newpts
	lines = lines + newlines
if debugOne: print "Number of Points: %d\nNumber of Lines: %d" % (len(pts), len(lines))
if debugOne: print
if debugOne: 
	for idx,pt in enumerate(pts):
		print "Point: %d is" % idx,
		print pt
if debugOne: 
	print 
	for idx,pt in enumerate(lines):
		print "Line: %d is" % idx,
		print pt

# yay now that all the things are calculated, lets draw. 
screen = pygame.display.set_mode((w, h))
for line in lines:
	pygame.draw.line(screen, lineColor, getPointWithOffset(pts[line[0]]), getPointWithOffset(pts[line[1]]), lineThickness)
pygame.display.flip()   # Flush pygame buffer

# Below code is to keep the window open after drawing. 
running = True
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
