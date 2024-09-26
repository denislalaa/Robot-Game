import turtle
import pygame
import player
from tkinter import *
from PIL import Image, ImageTk

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
    sc.bgpic("bg1.png")  # Set the background image

    # Define boundaries for the player
    boundaries = {
        'left': -360,
        'right': 360,
    }
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

    # Create the barrier and door
    barrier1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200))
    door_ = player.Barrier(gif_file=r".\\assets\\door_.gif", position=(330, -155))

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

    # Function to move to the next level (Level 2)
    def go_to_level_2():
        global level
        level = 2  # Update level to 2

        sc.clearscreen()
        sc.title("Level 2")
        sc.setup(width=800, height=600)

        sc.bgpic("bg_2.gif")
        sc.update()

        maze = turtle.Turtle()
        maze.penup()
        maze.pensize(2)
        maze.goto(360, 210)
        maze.pendown()
        maze.goto(360, -210)
        maze.goto(-360, -210)
        maze.goto(-360, 210)
        maze.goto(360, 210)
        maze.penup()
        maze.goto(-360, 0)
        maze.pendown()
        maze.goto(360, 0)
        maze.hideturtle()

        # Existing barriers
        port_bottom = player.Barrier(gif_file=r".\\assets\\port1.gif", position=(330, -190))
        port_top = player.Barrier(gif_file=r".\\assets\\port2.gif", position=(-330, 30))
        electric_1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200))


        box = player.Barrier(gif_file=r".\\assets\\box.gif", position=(0, 30))  # Box on the second floor

        # Continue with the rest of the function...
        robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
        robot.t.goto(-330, -190)
        global door_level_2  # Define the door for level 2
        door_level_2 = player.Barrier(gif_file=r".\\assets\\door_.gif", position=(330, 55))


        port_bottom = player.Barrier(gif_file=r".\\assets\\port1.gif", position=(330, -190))
        port_top = player.Barrier(gif_file=r".\\assets\\port2.gif", position=(-330, 30))
        electric_1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200))

        # Create and position the robot
        robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
        robot.t.goto(-330, -190)
        global door_level_2  # Define the door for level 2
        door_level_2 = player.Barrier(gif_file=r".\\assets\\door_.gif", position=(330, 55))

        # Function to check if robot has reached the door in Level 2

        def teleport_up():
            robot.t.goto(-330, 20)
            robot.ground_level = 30
            robot.y_speed = 0
            robot.is_jumping = False
            print("Teleported Up!")

        def teleport_down():
            robot.t.goto(330, -190)
            robot.ground_level = -190
            robot.y_speed = 0
            robot.is_jumping = False
            print("Teleported Down!")

        # Check teleportation zones
        def check_teleport():
            if robot.t.distance(port_bottom.t) < 30:
                sc.onkeypress(teleport_up, "Up")
            elif robot.t.distance(port_top.t) < 30:
                sc.onkeypress(teleport_down, "Down")
            else:
                sc.onkeypress(None, "Up")
                sc.onkeypress(None, "Down")

            sc.ontimer(check_teleport, 100)

        # Check if robot touches the barrier
        def check_barrier_collision():
            if robot.check_collision(electric_1):
                print("Touched the barrier! Restarting position...")
                robot.t.goto(-330, -190)

            sc.ontimer(check_barrier_collision, 100)

        # Check if robot has reached the door to level 3
        def check_collisions_level_2():
            check_door_level_2()  # Check if robot has reached the door to level 3
            check_barrier_collision()  # Check if robot touches any barrier

        sc.listen()
        sc.onkeypress(robot.go_left, "Left")
        sc.onkeypress(robot.go_right, "Right")
        sc.onkeypress(robot.jump, "space")

        check_teleport()
        check_collisions_level_2()  # Start collision checks for level 2

        robot.update_jump()

    # Function to move to Level 3
    def go_to_level_3():
        global level
        level = 3  # Update level to 3

        # Setup the turtle screen
        sc.clearscreen()
        sc.bgcolor("lightgreen")  # Change background color for Level 3
        sc.title("Level 3")  # Update title for Level 3

        boundaries = {
            'left': -360,
            'right': 360,
        }

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

        # Draw the horizontal lines for the floors
        for i in range(0, 4):
            maze.penup()
            maze.goto(-360, 140 * i)
            maze.pendown()
            maze.goto(360, 140 * i)

        maze.hideturtle()  # Hide the turtle after drawing

        # Reposition the robot for level 3
        robot.t.goto(-330, 270)  # Set robot's starting position at the third floor

        # Set up keyboard bindings
        sc.listen()
        sc.onkeypress(robot.go_left, "Left")  # Move left
        sc.onkeypress(robot.go_right, "Right")  # Move right
        sc.onkeypress(robot.jump, "space")  # Jump when spacebar is pressed

        # Start the gravity and jump updates
        robot.update_jump()  # Ensure the jump function is called

    # Function to check if robot has reached the door in Level 1
    def check_door():
        if robot.check_collision(door_):  # Check if robot has reached the door
            print(f"Robot Position: {robot.t.position()}, Door Position: {door_.t.position()}")
            print("Reached the door! Moving to Level 2...")
            door_.t.hideturtle()  # Hide the door so it can't be checked again
            go_to_level_2()  # Move to the second level

    def check_door_level_2():
        # Define the door coordinates
        door_x, door_y = 330, 55
        distance_threshold = 30  # Define how close the robot needs to be to the door

        # Check the distance between the robot and the door
        if abs(robot.t.xcor() - door_x) < distance_threshold and abs(robot.t.ycor() - door_y) < distance_threshold:
            print("Reached the door! Moving to Level 3...")
            go_to_level_3()  # Move to the third level

    # Function to check collisions in Level 1
    def check_collisions():
        if level == 1:
            if robot.check_collision(barrier1):  # Check if robot touches the barrier
                print("Touched the barrier! Restarting position...")
                robot.t.goto(-330, -190)  # Restart the level on collision
            else:
                check_door()  # Check if robot has reached the door

        turtle.Screen().ontimer(check_collisions, 100)  # Re-check every 100ms

    check_collisions()  # Start collision checks for level 1


# Global variable to store player speed
player_speed = 5  # Default speed


# Function to open a new window for options
def open_options():
    global player_speed  # Access the global player_speed variable
    # Dritarja e window
    options_window = Toplevel(window)
    options_window.title("Options")
    options_window.geometry("400x400")

    Label(options_window, text="Adjust Player Speed", font=("Comic Sans MS", 18)).pack(pady=20)

    # Initialize the scale with the current player speed
    speed_var = IntVar(value=player_speed)  # Use the global variable
    speed_scale = Scale(options_window, from_=1, to=10, orient=HORIZONTAL, variable=speed_var)
    speed_scale.pack(pady=20)

    # Funksion qe te ruaje speed level
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
music_button = Button(window, image=music_image, bg='#262d5c')
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
button2 = Button(window, text="Start", font=("Comic Sans MS", 28), bg='#262d5c', fg='black', compound="center",
                 command=start_game)
button2.place(x=center_label(button2, window_width), y=200)
button2.bind("<Enter>", lambda e: highlight_label(button2))

button1 = Button(window, text="Options", font=("Comic Sans MS", 28), bg='#262d5c', fg='black', compound="center",
                 command=open_options)
button1.place(x=center_label(button1, window_width), y=300)
button1.bind("<Enter>", lambda e: highlight_label(button1))

button = Button(window, text="Exit", font=("Comic Sans MS", 28), bg='#262d5c', fg='black', compound="center",
                command=exit_game)
button.place(x=center_label(button, window_width), y=400)
button.bind("<Enter>", lambda e: highlight_label(button))

# Start the Tkinter main loop
window.mainloop()
