import turtle
import pygame
import player
from tkinter import *

# List to store doors
doors = []


# Function to move to the next level (Level 3)
def go_to_level_3():
    global level
    sc = turtle.Screen()
    level = 3  # Update level to 3
    sc.clearscreen()
    sc.bgcolor("lightgreen")  # Change background color for Level 3
    sc.title("Niveli 3")  # Update title for Level 3

    # Setup the turtle screen
    sc.setup(width=800, height=600)
    sc.bgpic("background_1.png")

    boundaries = {
        'left': -360,
        'right': 360,
    }

    # Create a turtle for drawing boundaries
    maze = turtle.Turtle()
    maze.penup()
    maze.pensize(2)
    maze.goto(360, 210)
    maze.pendown()
    maze.goto(360, -210)
    maze.goto(-360, -210)
    maze.goto(-360, 210)
    maze.goto(360, 210)
    maze.hideturtle()

    # Draw the horizontal lines for the floors
    maze.penup()
    maze.goto(-360, -70)  # First floor
    maze.pendown()
    maze.goto(360, -70)

    maze.penup()
    maze.goto(-360, 70)  # Second floor
    maze.pendown()
    maze.goto(360, 70)

    maze.hideturtle()  # Hide the turtle after drawing

    # Create barriers and doors
    barrier1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(-180, -200))

    door_positions = [(300, -155), (200, -100)]  # Valid door positions
    for pos in door_positions:
        door = player.Barrier(gif_file=r".\\assets\\door_.gif", position=pos)  # Use the correct image for doors
        doors.append(door)

    # Reposition the robot for level 3
    robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)  # Set robot's starting position

    # Set up keyboard bindings
    sc.listen()
    sc.onkeypress(robot.go_left, "Left")  # Move left
    sc.onkeypress(robot.go_right, "Right")  # Move right
    sc.onkeypress(robot.jump, "space")  # Jump when spacebar is pressed

    # Start the gravity and jump updates
    robot.update_jump()  # Ensure the jump function is called


# Function to check if the robot has reached any door
def check_doors():
    for door in doors:
        if robot.check_collision(door):  # Check collision with each door
            print("Robot reached a door")
            door.t.hideturtle()  # Hide the door if it's reached
            # Handle level transition or other logic here
            # For example, call the next level function if this is the last door
            # go_to_next_level()  # Define this function as needed


# Function to check all collisions
def check_collisions():
    # Include other collision checks if necessary
    check_doors()  # Check for door collisions
    turtle.Screen().ontimer(check_collisions, 100)  # Schedule the next check


# Start checking for collisions when level 3 is activated
turtle.Screen().ontimer(check_collisions, 100)
