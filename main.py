import turtle
import player

# Ensure this is your player.py file with Player and Barrier classes
from tkinter import *

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

# Function to start the first level
def start_game():
    window.withdraw()  # Hide the Tkinter window
    print("Starting Level 1...")  # Debugging

    # Setup the turtle screen
    sc = turtle.Screen()
    sc.title("Level 1")
    sc.setup(width=1200, height=600)
    sc.bgcolor("white")  # Set a background color to ensure visibility

    # Define boundaries for the player
    boundaries = {
        'left': -360,
        'right': 360,
    }

    # Create the barrier
    barrier1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200))

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

    # Create and position

    robot = player.Player(gif_file=r"assets\\roboti.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)  # Set robot's starting position

    # Set up keyboard bindings
    sc.listen()
    sc.onkey(robot.go_left, "Left")  # Move left
    sc.onkey(robot.go_right, "Right")  # Move right
    sc.onkey(robot.jump, "space")  # Jump when spacebar is pressed

    # Start the gravity and jump updates

    robot.update_jump()

    def check_collisions():
        if robot.check_collision(barrier1):
            print("Level Failed")
            robot.t.goto(-330, -190) # Restart the level on collision


        turtle.Screen().ontimer(check_collisions, 100)

    check_collisions()



# Function to open a new window for options
def open_options():
    options_window = Toplevel(window)
    options_window.title("Options")
    options_window.geometry("400x400")

    Label(options_window, text="Adjust Player Speed", font=("Comic Sans MS", 18)).pack(pady=20)

    speed_var = IntVar(value=5)
    Scale(options_window, from_=1, to=10, orient=HORIZONTAL, variable=speed_var).pack(pady=20)

    def save_options():
        print(f"Player speed set to: {speed_var.get()}")
        options_window.destroy()

    Button(options_window, text="Save", command=save_options).pack(pady=10)

# Function to exit the game
def exit_game():
    turtle.bye()  # Close the turtle window
    window.quit()  # Close the Tkinter window

# Create the main window
window = Tk()
window.title("Circuit Runner")

# Enable fullscreen mode
window.attributes("-fullscreen", True)

# Bind the Escape key to exit fullscreen mode
window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

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
