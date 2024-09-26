import turtle
import pygame
class Player:
    def __init__(self, gif_file=r"assets\\roboti.gif", boundaries=None):
        turtle.register_shape(gif_file)
        self.t = turtle.Turtle()
        self.t.shape(gif_file)
        self.t.penup()
        self.t.speed(0)
        self.points = 0
        self.speed = 20  # Movement speed
        self.jump_height = 150  # Max height of the jump
        self.gravity = 3  # Gravity effect
        self.is_jumping = False  # Jumping status
        self.jump_velocity = 30  # Jump speed
        self.velocity_y = 0  # Player's vertical velocity
        self.ground_level = -190  # Ground level Y-coordinate
        self.boundaries = boundaries  # Boundaries of the playable area

        # Start player at the ground level
        self.t.sety(self.ground_level)

    def go_left(self):
        new_x = self.t.xcor() - self.speed
        if self.boundaries is None or new_x >= self.boundaries['left'] + 10:
            self.t.setx(new_x)

    def go_right(self):
        new_x = self.t.xcor() + self.speed
        if self.boundaries is None or new_x <= self.boundaries['right'] - 10:
            self.t.setx(new_x)

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity_y = self.jump_velocity
            pygame.mixer.Sound(r".\\sound\\jump.wav").play()  # Play jump sound

    def update_jump(self):
        if self.is_jumping:
            self.t.sety(self.t.ycor() + self.velocity_y)
            self.velocity_y -= self.gravity

            if self.t.ycor() <= self.ground_level:
                self.t.sety(self.ground_level)
                self.is_jumping = False
                self.velocity_y = 0

        if not self.is_jumping and self.t.ycor() > self.ground_level:
            self.t.sety(self.t.ycor() - self.gravity)

        turtle.Screen().ontimer(self.update_jump, 20)

    def check_collision(self, barrier):
        return self.t.distance(barrier.t) < 50


class Barrier:
    def __init__(self, gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200)):
        turtle.register_shape(gif_file)
        self.t = turtle.Turtle()
        self.t.shape(gif_file)
        self.t.penup()
        self.t.goto(position)
        self.t.speed(0)
