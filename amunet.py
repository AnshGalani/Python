import turtle 
import math
from time import strftime
from random import *

### Setting up Osiris' Window

wn = turtle.Screen()
osiris = turtle.Turtle()
wn.screensize(10000, 10000)
djet = strftime("%Y-%m-%d %H-%M-%S")

### SCREENSHOT COMMAND ON 'A' KEYBOARD PRESS ###

def ihy():
    ts = osiris.getscreen()
    osiris.hideturtle()
    ts.getcanvas().postscript(file="horus - " + djet +
                              ".eps", width=5000, height=5000)
    osiris.showturtle()
    print ('screenshot taken')
turtle.onkey(ihy,"a")
turtle.listen()

### CENTRE DOT COMMAND ON 'D' KEYBOARD PRESS ###

def yam():
    osiris.penup()
    osiris.goto(0,0)
    osiris.dot(3,'#0000FF')
    
turtle.onkey(yam,"d")
turtle.listen()

'''
#############################################################
################## GEOMETRIC DEFINITIONS ####################
##################        START          ####################
#############################################################
'''

########################
### Amunet = Diamond ###
### Creation Godess  ###   
########################
### Developed using
### 1,20,200,9,'#FF4444

def amunet(amunet_y=1,amunet_start=20,amunet_size=200,
           amunet_pensize=9,amunet_color='#FF4444'):
    if amunet_y == 1:
        osiris.forward(amunet_start)
        osiris.pensize(amunet_pensize)
        osiris.color(amunet_color)
        osiris.pendown()
        osiris.right(45)
        osiris.forward(amunet_size)
        for b in range(1,4):
            osiris.left(90)
            osiris.forward(amunet_size)
            if b == 1:
                osirisCurrentX = osiris.xcor()  
                osirisCurrentY = osiris.ycor()
        osiris.penup()
        osiris.goto(osirisCurrentX, osirisCurrentY)    
        osiris.setheading(osirisHeadingStart)


'''
##############################################
##############################################
##################START#######################
##############################################
##############################################
'''
    
	#####################
	#CONFIGURING OSIRIS##
	#####################

osiris.speed(2)
def osirisslow():
    osiris.speed(1)
def osirismid():
    osiris.speed(4)
def osirisquick():
    osiris.speed(0)
turtle.onkey(osirisquick,"0")
turtle.onkey(osirismid,"4")
turtle.onkey(osirisslow,"1")
turtle.listen()
osiris.penup()
osiris.setheading(90)
osirisHeadingStart = osiris.heading()
osiris.goto(0,0)

################
#ROTATE SECTION#
################

### SHU         ### CONTROLS THE AMOUNT OF ROTATIONS

shu = 6

# if you want these on different diagonals - remember to divide it by SHU.
# EG.   First round = 90 when shu = 6
#       Second round = 60 when shu = 6
osiris.setheading(90)
for shu_a in range(shu):
    osiris.penup()             
    osiris.goto(0,0)
    osiris.forward(50)   
    osirisHeadingStart = osiris.heading()  
    osirisStartingX = osiris.xcor()
    osirisStartingY = osiris.ycor()

### AMUNET      ### DIAMOND
    amunet(amunet_y=1,amunet_start=20,amunet_size=100,
           amunet_pensize=9,amunet_color='#FF4444')
    
###################
#COMMAND TO ROTATE#
###################

    osiris.setheading(osirisHeadingStart)
    osirisHeadingStart = osirisHeadingStart + (360/shu)
    osiris.setheading(osirisHeadingStart)

'''
##################################
##################################
################END###############
##################################
##################################
'''

turtle.done()