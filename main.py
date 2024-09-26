import turtle
import pygame
import barrier
import player
# Ensure this is your player.py file with Player and Barrier classes
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

# Function to start the first level
def start_game():
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

    # Create the barrier
    barrier1 = barrier.Barrier(gif_file=r".\\assets\\electric_1.gif", position=(0, -200))

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
    robot = player.Player(gif_file=r"C:\\Users\\Asus\\Downloads\\robot.gif", boundaries=boundaries)
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
            robot.t.goto(-330, -190)  # Restart the level on collision

        turtle.Screen().ontimer(check_collisions, 100)

    check_collisions()  # Start checking for collisions

def restart_level():
    turtle.clearscreen()  # Clear the screen
    start_game()  # Restart the level

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


def volume_down():
    global volume_muted
    if volume_muted:
        pygame.mixer.music.set_volume(1.0)  # Rikthejmë volumin
        volume_muted = False  # Ndryshojmë gjendjen në të kundërt
    else:
        pygame.mixer.music.set_volume(0.0)  # Ulim volumin
        volume_muted = True


# Create the main window
window = Tk()
window.title("Circuit Runner")
window.geometry('800x800')



# Bind the Escape key to exit fullscreen mode
window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))



# Ngarkojmë foton e sfondit
background_image = PhotoImage(file="background.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ngarkojmë ikonën e muzikës dhe e vendosim në këndin e siperm djathtas
music_image = PhotoImage(file="music.png")
music_button = Button(window, image=music_image, bg='#1f3659')  # Mund të vendosësh sfondin për të kombinuar me dritaren
music_button.place(x=700, y=50)  # Pozicionohet në këndin e poshtëm djathtas
music_button.bind('<Enter>', lambda e: highlight_label(music_button))
music_button.bind('<Button-1>', lambda e: volume_down())

# Vendosim muziken ne bg duke perdorur efektet e gatshme te pygame
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
