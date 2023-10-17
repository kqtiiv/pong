from turtle import Turtle
FONT = ("Arial", 20, "normal")
WIN_CONDITION = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 250)
        self.clear()
        self.write(self.left_score, align="center", font=FONT)
        self.goto(100, 250)
        self.write(self.right_score, align="center", font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()

    def game_over(self):
        if self.right_score == WIN_CONDITION:
            self.goto(0, 0)
            self.write("Player 2 Wins!", align="center", font=FONT)
            return True
        elif self.left_score == WIN_CONDITION:
            self.goto(0, 0)
            self.write("Player 1 Wins!", align="center", font=FONT)
            return True
        return False
