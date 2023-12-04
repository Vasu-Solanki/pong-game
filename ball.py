from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("white")
        self.home()
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def ball_go(self):
        """It will help to move the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.speed("slow")
        self.goto(new_x, new_y)

    def hit_wall(self):
        # In this we change the ball quarter I to IV.
        self.y_move *= -1

    def hit_paddle(self):
        """If the ball hit by paddle, it will reflect the ball."""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def miss(self):
        """If the ball misses by any paddle, it will set the ball to the origin and throw it to the other player."""
        self.home()
        self.y_move *= -1
        self.x_move *= -1
        self.ball_go()
        self.ball_speed = 0.1
