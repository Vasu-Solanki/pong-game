from turtle import Turtle, Screen
screen = Screen()


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=5)
        self.penup()
        self.goto(position, 0)

    def controller(self, key_for_up, key_for_down):
        def go_up():
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

        def go_down():
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

        screen.listen()
        screen.onkeypress(go_up, key_for_up)
        screen.onkeypress(go_down, key_for_down)
