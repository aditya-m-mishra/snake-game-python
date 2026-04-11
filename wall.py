from turtle import Turtle


class Wall(Turtle):
    def __int__(self):
        super().__init__()
        self.wall = Turtle()
        self.wall.hideturtle()
        self.wall.penup()
        self.wall.color("white")
        self.wall.pensize(3)
        self.draw()

    def draw(self):
        self.wall.goto(-300, -300)
        self.wall.pendown()
        for _ in range(4):
            self.wall.forward(600)
            self.wall.left(90)
