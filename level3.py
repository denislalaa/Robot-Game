import turtle
import pygame
import player
from tkinter import *

# Function to move to the next level (Level 3)
def go_to_level_3():
    global level
    level = 3  # Update level to 3
    sc.clearscreen()
    sc.bgcolor("lightgreen")  # Change background color for Level 3
    sc.title("Niveli 3")  # Update title for Level 3

    # Create a turtle for drawing boundaries
    maze = turtle.Turtle()
    maze.penup()
    maze.pensize(2)

    # Draw the outer rectangle for the first floor
    maze.goto(360, 210)
    maze.pendown()
    maze.goto(360, -210)
    maze.goto(-360, -210)
    maze.goto(-360, 210)
    maze.goto(360, 210)

    # Draw the horizontal line for the first floor
    maze.penup()
    maze.goto(-360, 0)  # Starting point of the line
    maze.pendown()
    maze.goto(360, 0)  # End point of the line

    # Draw the horizontal line for the second floor
    maze.penup()
    maze.goto(-360, 140)  # Starting point of the line for the second floor
    maze.pendown()
    maze.goto(360, 140)  # End point of the line for the second floor

    # Draw the horizontal line for the third floor
    maze.penup()
    maze.goto(-360, 280)  # Starting point of the line for the third floor
    maze.pendown()
    maze.goto(360, 280)  # End point of the line for the third floor

    maze.hideturtle()  # Hide the turtle after drawing

    # Reposition the robot for level 3
    robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
    robot.t.goto(-330, 270)  # Set robot's starting position at the third floor

    # Set up keyboard bindings
    sc.listen()
    sc.onkeypress(robot.go_left, "Left")  # Move left
    sc.onkeypress(robot.go_right, "Right")  # Move right
    sc.onkeypress(robot.jump, "space")  # Jump when spacebar is pressed

    # Start the gravity and jump updates
    robot.update_jump()  # Ensure the jump function is called

