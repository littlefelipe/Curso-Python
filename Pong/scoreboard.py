from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 48, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(position)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)