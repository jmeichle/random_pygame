This repo holds random pygame code for 2D graphics rendering

## gauge.py

This is a simple example of a 'gauge' drawn on a pygame screen. It draws a circle, designates 160 degrees of it for the gauge value, draws labeled hash marks for 0-100 in steps of 10, and then plots 0-100-0 on a loop. Using threads, this could be used as a real time gauge of a value (scaled 0-100 int).

## color_grid.py

This is a simple app to render an array containing a 2D board of 'colors'. This is meant as helper code to visualize a grid of colors on a computer, with the eventual goal of having LED hardware display these same arrays. This program generates boards on the fly, and updates the pygame screen with them via the use of a worker thread and a queue. When the LED hardware is setup, this will be used to send data to the LED hardware for display.

## cubes.py

This is a simple app that draws a wireframe high dimensional cube. The single CLI argument is to specify the dimensionality of the cube, and a unique cube is drawn each time. The angles are automatically generated using an (awful) algorithm.

## cubes_loop.py

Same as cubes.py but on a loop.
