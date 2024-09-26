import turtle
import pygame
import player
from tkinter import *

# Function to move to level 3
def go_to_level_3(sc=None, boundaries=None):
    global level
    level = 3  # Update level to 3
    sc.clearscreen()  # Clear the screen for the new level
    sc.bgcolor("lightgreen")  # Set a different background color for level 3
    sc.title("Niveli 3")  # Set the title for level 3

 # Krijimi i barrierave per nivelin 3
    barrier2 = player.Barrier(gif_file=r".\\assets\\new_barrier.gif", position=(0, -100))  # Example barrier
    door_3 = player.Barrier(gif_file=r".\\assets\\door_3.gif", position=(330, -155))  # New door for level 3

    # Create and position robot for level 3
    robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)  # Set robot's starting position for level 3

    # Set up keyboard bindings for level 3
    sc.listen()
    sc.onkeypress(robot.go_left, "Left")
    sc.onkeypress(robot.go_right, "Right")
    sc.onkeypress(robot.jump, "space")

