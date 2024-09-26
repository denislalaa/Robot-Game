import turtle
import pygame
import player
from tkinter import *
from PIL import Image, ImageTk

volume_muted = False

# Funksion për të qendruar etiketat në mes
def center_label(label, window_width):
    label_width = label.winfo_reqwidth()
    x_position = (window_width - label_width) // 2
    return x_position

# Funksion për të ndriçuar etiketat kur kalon miu mbi to
def highlight_label(label):
    original_color = label.cget("bg")
    label.config(bg="white")
    label.after(200, lambda: label.config(bg=original_color))

# Variabël globale për të ruajtur nivelin aktual
level = 1

# Funksion për të nisur lojën (Niveli 1)
def start_game():
    global level
    window.withdraw()  # Fsheh dritaren Tkinter

<<<<<<< HEAD
    # Konfigurimi i ekranit Turtle për Niveli 1
    sc = turtle.Screen()
    sc.title("Level 1")
    sc.setup(width=800, height=600)
    sc.bgpic("background_1.png")
=======


    # Setup the turtle screen
    sc = turtle.Screen()
    sc.title("Level 1")
    sc.setup(width=800, height=600)
    sc.bgpic("bg1.png")  # Set the background image
>>>>>>> 6c1edecd37e757216b3474ddfde82c0b5d26656d

    # Përcakto kufijtë për lojtarin
    boundaries = {'left': -360, 'right': 360}

    # Krijo pengesën dhe derën
    barrier1 = player.Barrier(gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200))
    door_ = player.Barrier(gif_file=r".\\assets\\door_.gif", position=(330, -155))

    # Vendos dhe krijo labirintin (optional)
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

    # Krijo dhe vendos robotin
    robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)

    # Vendos tastierën
    sc.listen()
    sc.onkeypress(robot.go_left, "Left")
    sc.onkeypress(robot.go_right, "Right")
    sc.onkeypress(robot.jump, "space")

    # Përditëso gravitetin dhe kërcimin
    robot.update_jump()

    # Funksioni për të kaluar në Niveli 2
    def go_to_level_2():
        global level
<<<<<<< HEAD
        level = 2  # Kalon në nivelin 2
        sc.clearscreen()
        sc.bgcolor("lightblue")
        sc.title("Niveli 2")

        # Kati i parë dhe vendosja e pengesave
=======
        level = 2  # Update level to 2

        # Create a new Turtle screen and set its properties
        sc = turtle.Screen()
        sc.clearscreen()
        sc.title("Level 2")
        sc.setup(width=800, height=600)  # Set up the window size to match the image size


        sc.bgpic("bg_2.gif")  # Load the resized background image
        sc.update()  # Update the screen to reflect the changes
>>>>>>> 6c1edecd37e757216b3474ddfde82c0b5d26656d
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
<<<<<<< HEAD
        maze.goto(-360, 0)
=======
        maze.color("white")
        maze.goto(-360, 0)  # Starting point of the line
>>>>>>> 6c1edecd37e757216b3474ddfde82c0b5d26656d
        maze.pendown()
        maze.goto(360, 0)
        maze.hideturtle()

        # Vendos teleportet dhe robotin
        port_bottom = player.Barrier(gif_file=r".\\assets\\port1.gif", position=(330, -190))
        port_top = player.Barrier(gif_file=r".\\assets\\port2.gif", position=(-330, 30))

        robot = player.Player(gif_file=r".\\assets\\roboti.gif", boundaries=boundaries)
        robot.t.goto(-330, -190)

        electric_1 = player.Barrier(gif_file=r".\\assets\\electric_1.gif", position=(0, -180))
        wall = player.Barrier(gif_file=r".\\assets\\wall.gif", position=(0, 10))

        # Funksionet për teleportimin lart dhe poshtë
        def teleport_up():
            robot.t.goto(-330, 10)
            robot.ground_level = 0
            sc.onkeypress(None, "Up")

        def teleport_down():
            robot.t.goto(330, -190)
            robot.ground_level = -190
            sc.onkeypress(None, "Down")

        # Funksion për të lëvizur pengesën elektrike
        def move_electric_barrier():
            x = electric_1.t.xcor()
            if x >= 100:
                electric_1.t.setx(x - 5)
            elif x <= -100:
                electric_1.t.setx(x + 5)
            sc.ontimer(move_electric_barrier, 50)

        move_electric_barrier()

        # Funksion për të kontrolluar teleportin
        def check_teleport():
            if robot.t.distance(port_bottom.t) < 30:
                sc.onkeypress(teleport_up, "Up")
            elif robot.t.distance(port_top.t) < 30:
                sc.onkeypress(teleport_down, "Down")
            sc.ontimer(check_teleport, 100)

        # Vendos tastierën për nivelin e dytë
        sc.listen()
        sc.onkeypress(robot.go_left, "Left")
        sc.onkeypress(robot.go_right, "Right")
        sc.onkeypress(robot.jump, "space")
        robot.update_jump()
        check_teleport()

    # Funksioni për të kontrolluar derën
    def check_door():
        if robot.check_collision(door_):
            door_.t.hideturtle()
            go_to_level_2()

    # Funksioni për të kontrolluar përplasjet
    def check_collisions():
        if level == 1:
            if robot.check_collision(barrier1):
                robot.t.goto(-330, -190)
            else:
                check_door()

        turtle.Screen().ontimer(check_collisions, 100)

    check_collisions()

<<<<<<< HEAD
# Funksioni për të hapur dritaren e opsioneve
=======
# Global variable to store player speed
player_speed = 5  # Default speed



# Function to open a new window for options
>>>>>>> 6c1edecd37e757216b3474ddfde82c0b5d26656d
def open_options():
    global player_speed
    options_window = Toplevel(window)
    options_window.title("Options")
    options_window.geometry("400x400")

    Label(options_window, text="Adjust Player Speed", font=("Comic Sans MS", 18)).pack(pady=20)
    speed_var = IntVar(value=player_speed)
    speed_scale = Scale(options_window, from_=1, to=10, orient=HORIZONTAL, variable=speed_var)
    speed_scale.pack(pady=20)

    def save_options():
        global player_speed
        player_speed = speed_var.get()
        options_window.destroy()

    Button(options_window, text="Save", command=save_options).pack(pady=10)

# Funksioni për të dalë nga loja
def exit_game():
    turtle.bye()
    window.quit()

# Funksioni për të ulur volumin
def volume_down():
    global volume_muted
    if volume_muted:
        pygame.mixer.music.set_volume(1.0)
        volume_muted = False
    else:
        pygame.mixer.music.set_volume(0.0)
        volume_muted = True

# Dritarja kryesore e lojës
window = Tk()
window.title("Circuit Runner")
window.geometry('800x800')

window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))
background_image = PhotoImage(file="background.png")
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

music_image = PhotoImage(file="music.png")
music_button = Button(window, image=music_image, bg='#262d5c')
music_button.place(x=700, y=50)
music_button.bind('<Button-1>', lambda e: volume_down())

pygame.mixer.init()
pygame.mixer.music.load("game_music.ogg")
pygame.mixer.music.play(-1)

window.update()
window_width = window.winfo_width()

<<<<<<< HEAD
button2 = Button(window, text="Start", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', command=start_game)
button2.place(x=center_label(button2, window_width), y=200)
button1 = Button(window, text="Options", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', command=open_options)
button1.place(x=center_label(button1, window_width), y=300)
button = Button(window, text="Exit", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', command=exit_game)
=======
# Create buttons and bind functions
button2 = Button(window, text="Start", font=("Comic Sans MS", 28), bg='#262d5c', fg='black', compound="center", command=start_game)
button2.place(x=center_label(button2, window_width), y=200)
button2.bind("<Enter>", lambda e: highlight_label(button2))

button1 = Button(window, text="Options", font=("Comic Sans MS", 28), bg='#262d5c', fg='black', compound="center", command=open_options)
button1.place(x=center_label(button1, window_width), y=300)
button1.bind("<Enter>", lambda e: highlight_label(button1))

button = Button(window, text="Exit", font=("Comic Sans MS", 28), bg='#262d5c', fg='black', compound="center", command=exit_game)
>>>>>>> 6c1edecd37e757216b3474ddfde82c0b5d26656d
button.place(x=center_label(button, window_width), y=400)

window.mainloop()
