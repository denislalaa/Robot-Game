import turtle

class Player:
    def __init__(self, gif_file=r"assets\\roboti.gif", boundaries=None):
        # Register the GIF file as a turtle shape
        turtle.register_shape(gif_file)
        self.t = turtle.Turtle()
        self.t.shape(gif_file)
        self.t.penup()  # Avoid leaving a trail
        self.t.speed(0)  # Fastest turtle speed
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
        new_x = self.t.xcor() - self.speed  # Calculate the new x-coordinate
        if self.boundaries is None or new_x >= self.boundaries['left'] + 10:  # Check if within left boundary
            self.t.setx(new_x)  # Move left

    def go_right(self):
        new_x = self.t.xcor() + self.speed  # Calculate the new x-coordinate
        if self.boundaries is None or new_x <= self.boundaries['right'] - 10:  # Check if within right boundary
            self.t.setx(new_x)  # Move right

    def jump(self):
        if not self.is_jumping:  # If the player isn't already jumping
            self.is_jumping = True
            self.velocity_y = self.jump_velocity  # Set upward velocity for jump

    def update_jump(self):
        if self.is_jumping:
            # Apply the upward movement
            self.t.sety(self.t.ycor() + self.velocity_y)
            # Reduce the upward velocity (simulate gravity)
            self.velocity_y -= self.gravity

            # Check if the player has landed on the ground
            if self.t.ycor() <= self.ground_level:
                self.t.sety(self.ground_level)  # Set player on ground level
                self.is_jumping = False  # Reset jump state
                self.velocity_y = 0  # Reset velocity after landing

        # Apply gravity if not jumping and player is above the ground level
        if not self.is_jumping and self.t.ycor() > self.ground_level:
            self.t.sety(self.t.ycor() - self.gravity)

        # Schedule the next update
        turtle.Screen().ontimer(self.update_jump, 20)

    def check_collision(self, barrier):
        # Example collision detection logic
        return self.t.distance(barrier.t) < 50  # Adjust threshold as needed


class Barrier:
    def __init__(self, gif_file=r".\\assets\\electric_barrier.gif", position=(0, -200)):

        turtle.register_shape(gif_file)
        self.t = turtle.Turtle()
        self.t.shape(gif_file)
        self.t.penup()
        self.t.goto(position)
        self.t.speed(0)
