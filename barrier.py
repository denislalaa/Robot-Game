import turtle

class Barrier:
    def __init__(self, gif_file=r".\\assets\\electric_1.gif", position=(-100, -200)):
        turtle.register_shape(gif_file)
        self.t = turtle.Turtle()
        self.t.shape(gif_file)
        self.t.penup()
        self.t.goto(position)
        self.t.speed(0)
