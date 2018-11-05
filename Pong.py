"""
    Pong Game (might make it cooler)
    Author: Jack Maloy
    Date: 11/4/18
"""
import sys
import os
import time
import turtle

#----- Global Variables -----#

playerSpeed = 15
computerSpeed = 10

#----- VISUALS NEEDED -----#

# Going to create a background for pong to be played
screen  = turtle.Screen()
screen.bgcolor("black")
screen.title("Pong")

# Player turtle
player = turtle.Turtle()
player.color("green")
player.shape("square")
player.shapesize(.5, 4)
player.tilt(90)
player.penup()
player.speed(0)
player.setposition(300, 0)

# Computer Turtle
comp = turtle.Turtle()
comp.color("green")
comp.shape("square")
comp.shapesize(.5, 4)
comp.tilt(90)
comp.penup()
comp.speed(0)
comp.setposition(-300, 0)


#----- Player movements -----#

def moveDown():
    if player.ycor() > -300:
        y = player.ycor()
        y -= playerSpeed
        player.sety(y)

def moveUp():
    if player.ycor() < 300:
        y = player.ycor()
        y += playerSpeed
        player.sety(y)
    

turtle.onkey(moveDown, "Down")
turtle.onkey(moveUp, "Up")
turtle.listen()

def updateComputer():
    
    if comp.ycor() > player.ycor():
        y = comp.ycor()
        y -= computerSpeed
        comp.sety(y)
    elif comp.ycor() < player.ycor():
        y = comp.ycor()
        y += computerSpeed
        comp.sety(y)
    else:
        #Dont really need to do anything
        y = comp.ycor()
        comp.sety(y)
        

#----- Main Loop -----#

while True:

    # Implement Computer following ball
    updateComputer()
        
    
    


delay = raw_input("Press enter to finish")



