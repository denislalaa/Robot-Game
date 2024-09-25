import turtle

class Player:
    def __init__(self, gif_file=r".\\assets\\robot.gif", boundaries=None):
        # Regjistro imazhin e robotit
        turtle.register_shape(gif_file)
        self.t = turtle.Turtle()
        self.t.shape(gif_file)
        self.t.penup()
        self.speed = 10
        self.jump_height = 100  # Lartësia e kërcimit
        self.gravity = 1  # Forca e gravitetit
        self.is_jumping = False  # Kontrollo nëse lojtari është duke kërcyer
        self.boundaries = boundaries or {'left': -360, 'right': 360}  # Kufijtë e lëvizjes

    def go_left(self):
        if self.t.xcor() > self.boundaries['left']:  # Kontrollo kufijtë
            self.t.setx(self.t.xcor() - self.speed)

    def go_right(self):
        if self.t.xcor() < self.boundaries['right']:  # Kontrollo kufijtë
            self.t.setx(self.t.xcor() + self.speed)

    def jump(self):
        if not self.is_jumping:  # Kontrollo nëse lojtari nuk është duke kërcyer
            self.is_jumping = True
            for _ in range(30):  # Kërcimi në lartësi
                self.t.sety(self.t.ycor() + self.jump_height / 30)
            for _ in range(30):  # Rënia pas kërcimit
                self.t.sety(self.t.ycor() - self.jump_height / 30)
            self.is_jumping = False

    def update_jump(self):
        if self.t.ycor() > 0:  # Rregullo pozitat nëse lojtari është mbi një nivel të caktuar
            self.t.sety(self.t.ycor() - self.gravity)  # Aplikoni gravitetin
