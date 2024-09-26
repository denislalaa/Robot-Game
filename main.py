import turtle
import player
import barrier

from tkinter import *

# Funksioni për qendrim të etiketave
def center_label(label, window_width):
    label_width = label.winfo_reqwidth()
    x_position = (window_width - label_width) // 2
    return x_position

# Funksioni për të theksuar etiketat gjatë hover
def highlight_label(label):
    original_color = label.cget("bg")
    label.config(bg="white")
    label.after(200, lambda: label.config(bg=original_color))

# Variablat globale për gjendjen e lojës
gameplay = 'idle'

# Funksioni për të nisur nivelin e parë
def start_game():
    global gameplay
    window.withdraw()  # Fshi dritaren Tkinter
    gameplay = 'active'  # Aktivizo lojën
    print("Duke nisur Nivelin 1...")

    # Konfigurimi i ekranit turtle
    sc = turtle.Screen()
    sc.title("Nivel 1")
    sc.setup(width=1200, height=600)
    sc.bgcolor("white")

    # Kufijtë për lojtarin
    boundaries = {
        'left': -360,
        'right': 360,
    }

    # Regjistro imazhet GIF
    turtle.register_shape(r".\\assets\\ghost.gif")
    turtle.register_shape(r".\\assets\\robot.gif")

    # Krijo barrierën dhe derën
    barrier1 = barrier.Barrier(gif_file=r".\\assets\\electric_1.gif", position=(0, -200))
    door = barrier.Barrier(gif_file=r".\\assets\\door.gif", position=(350, -190))

    # Krijo fantazmën
    ghost = turtle.Turtle()
    ghost.shape(r".\\assets\\ghost.gif")
    ghost.penup()
    ghost.hideturtle()

    # Krijo dhe poziciono robotin
    robot = player.Player(gif_file=r".\\assets\\robot.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)

    # Konfigurimi i lidhjeve të tastierës
    sc.listen()
    sc.onkey(robot.go_left, "Left")
    sc.onkey(robot.go_right, "Right")
    sc.onkey(robot.jump, "space")  # Sigurohuni që kërcimi është aktiv

    # Loop i lojës
    while True:
        if gameplay == 'active':
            robot.update_jump()  # Përditëso pozitat e robotit
            if check_collision(robot.t, barrier1, ghost):  # Kontrollo përplasjen me barrierën
                display_lose_message()  # Shfaq mesazhin e humbjes
            check_door(robot.t, door)  # Kontrollo nëse robot arriti derën
        sc.update()

# Funksioni për të kontrolluar përplasjen me barrierën elektrike
def check_collision(robot, barrier1, ghost):
    if robot.distance(barrier1.t) < 30:  # Kontrollo distancën për përplasjen
        print("Përplasje e zbuluar! Ju humbët!")  # Linja për debugging
        ghost.goto(robot.xcor(), robot.ycor())  # Vendos fantazmën në pozitat e robotit
        ghost.showturtle()  # Trego fantazmën
        return True
    return False

# Funksioni për të shfaqur mesazhin e humbjes
def display_lose_message():
    global gameplay
    gameplay = 'paused'  # Ndalo lojën

    # Krijo mesazhin e humbjes
    lose_message = turtle.Turtle()
    lose_message.hideturtle()
    lose_message.penup()
    lose_message.color("red")
    lose_message.goto(0, 0)  # Qendro në mes
    lose_message.write("JU HUMBËT", align="center", font=("Arial", 36, "bold"))

# Funksioni për të kontrolluar nëse lojtari arrin derën
def check_door(robot, door):
    if robot.distance(door.t) < 20:  # Kontrollo nëse lojtari është afër derës
        print("Robot arriti derën! Kalimi në nivelin e dytë...")
        go_to_level_2()  # Thirri funksionin që kalon në nivelin e dytë

# Funksioni për të kaluar në Nivelin 2
def go_to_level_2():
    sc = turtle.Screen()
    sc.clearscreen()  # Pastrimi i ekranit
    sc.bgcolor("lightblue")  # Ngjyra e sfondit për Nivelin 2
    sc.title("Nivel 2")

    # Krijo kufijtë për nivelin e dytë
    boundaries = {
        'left': -360,
        'right': 360,
    }

    # Krijo barrierat dhe robotin për nivelin e dytë
    barrier2 = barrier.Barrier(gif_file=r".\\assets\\electric_1.gif", position=(100, -200))
    robot = player.Player(gif_file=r".\\assets\\robot.gif", boundaries=boundaries)
    robot.t.goto(-330, -190)  # Vendosja e pozitatit të robotit për nivelin e dytë

    # Shtoni komandat për lëvizjen e robotit
    sc.listen()
    sc.onkey(robot.go_left, "Left")
    sc.onkey(robot.go_right, "Right")
    sc.onkey(robot.jump, "space")

# Funksioni për të hapur një dritare të re për opsione
def open_options():
    options_window = Toplevel(window)
    options_window.title("Opsione")
    options_window.geometry("400x400")

    Label(options_window, text="Rregullo Shpejtësinë e Lojtarit", font=("Comic Sans MS", 18)).pack(pady=20)

    speed_var = IntVar(value=5)
    Scale(options_window, from_=1, to=10, orient=HORIZONTAL, variable=speed_var).pack(pady=20)

    def save_options():
        print(f"Shpejtësia e lojtarit është vendosur në: {speed_var.get()}")
        options_window.destroy()

    Button(options_window, text="Ruaj", command=save_options).pack(pady=10)

# Funksioni për të dalë nga loja
def exit_game():
    turtle.bye()  # Mbylle dritaren e turtle
    window.quit()  # Mbylle dritaren Tkinter

# Krijo dritaren kryesore
window = Tk()
window.title("Circuit Runner")

# Aktivizo modin e ekranit të plotë
window.attributes("-fullscreen", True)

# Lidhu çelësi Escape për të dalë nga moda e plotë
window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

# Përditëso madhësinë e dritares
window.update()
window_width = window.winfo_width()

# Krijo butona dhe lidhu funksionet
button2 = Button(window, text="Nis", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', compound="center",
                 command=start_game)
button2.place(x=center_label(button2, window_width), y=200)
button2.bind("<Enter>", lambda e: highlight_label(button2))

button1 = Button(window, text="Opsione", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', compound="center",
                 command=open_options)
button1.place(x=center_label(button1, window_width), y=300)
button1.bind("<Enter>", lambda e: highlight_label(button1))

button = Button(window, text="Dal", font=("Comic Sans MS", 28), bg='#1f3659', fg='black', compound="center",
                command=exit_game)
button.place(x=center_label(button, window_width), y=400)
button.bind("<Enter>", lambda e: highlight_label(button))

# Filloni loopin kryesor të Tkinter
window.mainloop()
