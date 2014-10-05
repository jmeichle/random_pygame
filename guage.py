#!/usr/bin/python
import pygame, time, sys, random, math
from pprint import pprint
from Queue import Queue
from threading import Thread

WORKER_THREAD_SLEEP_TIME = 0.5
DISPLAY_LOOP_SLEEP_TIME = 0.01

white = (255,255,255)

# The total size of the window to draw. The window will be a square of (size x size)
size = 800

pygame.init()
# create the pygame screen of the given size.
screen = pygame.display.set_mode((size, size))

# x,y
circle_center = (size/2, size/2)
circle_radius = size/4

# Draw a circle, and a line from the center to the passed degrees argument.
def draw_circle_with_line(degree, screen):
  screen.fill( (0,0,0) )
  pygame.draw.circle(screen, white, circle_center, circle_radius, 2)
  pygame.draw.lines(screen, white, False, [circle_center, get_point_on_circle(degree)], 2)

def get_point_on_circle(degree, offset = 0):
  radians = math.radians(degree)
  x = ((circle_radius+offset) * math.cos(radians)) + circle_center[0]
  y = ((circle_radius+offset) * math.sin(radians)) + circle_center[1]
  return (x,y)

dash_length = 10
def get_dash_on_circle_edge(degree):
  one = get_point_on_circle(degree, (0+dash_length/2))
  two = get_point_on_circle(degree, (0-dash_length/2))
  return (one,two)

def draw_dash_value(value, screen):
  myfont = pygame.font.SysFont("monospace", 30)
  
  label = myfont.render(str(value), 1, (255,255,0))
  degree = get_normalized_guage_point(value)
  pt = get_point_on_circle(degree, 50)
  screen.blit(label, pt)

def get_normalized_guage_point(value):
  min_point = 180-30 # degree of zero.
  # value from 0-100 scaled to 0-160
  normalized_value = (float(value)/100.0)*160.0
  # add normalized_value to min_point
  return (min_point+normalized_value)

def get_gauge_marker_lines():
  # ok, 0 degrees is to the right. we want to the left, minus a bit (30 degrees)
  return []

# This takes a value (0 - 100) and displays it on a circular guage
def draw_guage_with_value(value, screen):
  screen.fill( (0,0,0) )
  pygame.draw.circle(screen, white, circle_center, circle_radius, 2)
  # # These are the gauge marks to indicate 0 - 100 on the circle
  # marker_lines = get_gauge_marker_lines()
  # pygame.draw.lines(screen, white, False, marker_lines, 2)
  point = get_point_on_circle(get_normalized_guage_point(value))
  print "point for value: %s is: (%s,%s)" % (value, point[0], point[1])
  pygame.draw.lines(screen, white, False, [circle_center, point], 2)
  for dash_tenth in range(0, 110, 10):
    points = get_dash_on_circle_edge(get_normalized_guage_point(dash_tenth))
    draw_dash_value(dash_tenth, screen)
    pygame.draw.lines(screen, white, False, points, 2)



# loop over reads from the queue, and when a board is received draw it. 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  for i in range(100):
    draw_guage_with_value(i, screen)
    pygame.display.flip()
    time.sleep(0.01)
  for i in range(100,0,-1):
    draw_guage_with_value(i, screen)
    pygame.display.flip()
    time.sleep(0.01)
