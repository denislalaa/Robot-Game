import turtle
import pygame
import player
from tkinter import *

volume_muted = False

# Function to center labels
def center_label(label, window_width):
    label_width = label.winfo_reqwidth()
    x_position = (window_width - label_width) // 2
    return x_position

# Function to highlight labels on hover
def highlight_label(label):
    original_color = label.cget("bg")
    label.config(bg="white")
    label.after(200, lambda: label.config(bg=original_color))

# Global variable to track level
level = 1

# Function to start the first level
def start_game():
    global level
    window.withdraw()  # Hide the Tkinter window
    print("Starting Level 1...")  # Debugging

    # Setup the turtle screen
    sc = turtle.Screen()
    sc.title("Level 1")
    sc.setup(width=800, height=600)
    sc.bgpic("background_1.png")  # Set the background image

    # Define boundaries for the player
    boundaries = {
        'left': -360,
        'right': 360,
    }

    # Create the barrier and door
    barrier1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200))
    door_ = player.Barrier(gif_file=r".\\assets\\door_.gif", position=(330, -155))

    # Create maze (optional)
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

    # Create and position robot
    robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)  # Set robot's starting position

    # Set up keyboard bindings
    sc.listen()
    sc.onkeypress(robot.go_left, "Left")  # Move left
    sc.onkeypress(robot.go_right, "Right")  # Move right
    sc.onkeypress(robot.jump, "space")  # Jump when spacebar is pressed

    # Start the gravity and jump updates
    robot.update_jump()

    # Function to move to level 2
    def go_to_level_2():
        global level
        level = 2  # Update level to 2
        sc.clearscreen()
        sc.bgcolor("lightblue")
        sc.title("Niveli 2")

        # First floor boundary
        maze = turtle.Turtle()
        maze.penup()
        maze.pensize(2)

        # Draw the first floor (outer rectangle)
        maze.goto(360, 210)
        maze.pendown()
        maze.goto(360, -210)
        maze.goto(-360, -210)
        maze.goto(-360, 210)
        maze.goto(360, 210)

        # Draw the second floor line (horizontal line inside the first floor)
        maze.penup()
        maze.goto(-360, 0)  # Starting point of the line
        maze.pendown()
        maze.goto(360, 0)  # End point of the line

        maze.hideturtle()

        # Reposition the robot for level 2
        robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
        robot.t.goto(-330, -190)  # Set robot's starting position

        # Set up keyboard bindings
        sc.listen()
        sc.onkeypress(robot.go_left, "Left")  # Move left
        sc.onkeypress(robot.go_right, "Right")  # Move right
        sc.onkeypress(robot.jump, "space")  # Jump when spacebar is pressed

        # Start the gravity and jump updates
        robot.update_jump()

    # Function to check if robot has reached the door
    def check_door():
        if robot.check_collision(door_):  # Check if robot has reached the door
            print("Roboti arriti te dera")
            door_.t.hideturtle()  # Hide the door so it can't be checked again
            go_to_level_2()  # Move to the second level

    # Function to check collisions
    def check_collisions():
        if level == 1:  # Only check collisions in level 1
            if robot.check_collision(barrier1):
                print("Level Failed")
                robot.t.goto(-330, -190)  # Restart the level on collision
            else:
                check_door()  # Check if robot has reached the door

        turtle.Screen().ontimer(check_collisions, 100)

    check_collisions()

# Global variable to store player speed
player_speed = 5  # Default speed

# Function to open a new window for options
def open_options():
    global player_speed  # Access the global player_speed variable
#Dritarja e window
    options_window = Toplevel(window)
    options_window.title("Options")
    options_window.geometry("400x400")

    Label(options_window, text="Adjust Player Speed", font=("Comic Sans MS", 18)).pack(pady=20)

    # Initialize the scale with the current player speed
    speed_var = IntVar(value=player_speed)  # Use the global variable
    speed_scale = Scale(options_window, from_=1, to=10, orient=HORIZONTAL, variable=speed_var)
    speed_scale.pack(pady=20)

#Funksion qe te ruaje speed level
    def save_options():
        global player_speed  # Use the global variable to store the speed
        player_speed = speed_var.get()  # Update the global player speed
        print(f"Player speed set to: {player_speed}")
        options_window.destroy()  # Close the options window

    Button(options_window, text="Save", command=save_options).pack(pady=10)


# Function to exit the game
def exit_game():
    turtle.bye()  # Close the turtle window
    window.quit()  # Close the Tkinter window

def volume_down():
    global volume_muted
    if volume_muted:
        pygame.mixer.music.set_volume(1.0)  # Reset volume
        volume_muted = False  # Change state back
    else:
        pygame.mixer.music.set_volume(0.0)  # Mute volume
        volume_muted = True

# Create the main window
window = Tk()
window.title("Circuit Runner")
window.geometry('800x800')

# Bind the Escape key to exit fullscreen mode
window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

# Load background image
background_image = PhotoImage(file="background.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load music icon and place it in the top right corner
music_image = PhotoImage(file="music.png")
music_button = Button(window, image=music_image, bg='#1f3659')
music_button.place(x=700, y=50)
music_button.bind('<Enter>', lambda e: highlight_label(music_button))
music_button.bind('<Button-1>', lambda e: volume_down())

# Set up background music using pygame
pygame.mixer.init()
pygame.mixer.music.load("game_music.ogg")
pygame.mixer.music.play(-1)

# Update window size
window.update()
window_width = window.winfo_width()

# Create buttons and bind functions
button2 = Button(window, text="Start", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', compound="center", command=start_game)
button2.place(x=center_label(button2, window_width), y=200)
button2.bind("<Enter>", lambda e: highlight_label(button2))

button1 = Button(window, text="Options", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', compound="center", command=open_options)
button1.place(x=center_label(button1, window_width), y=300)
button1.bind("<Enter>", lambda e: highlight_label(button1))

button = Button(window, text="Exit", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', compound="center", command=exit_game)
button.place(x=center_label(button, window_width), y=400)
button.bind("<Enter>", lambda e: highlight_label(button))

# Start the Tkinter main loop
window.mainloop()
