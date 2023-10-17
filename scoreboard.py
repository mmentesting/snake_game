from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.sety(180)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.lives = 3
        self.scoreboard_score()

    def scoreboard_score(self):
        self.clear()
        self.write(f"lives:{self.lives}    Score:{self.score}"
                   f"  High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.scoreboard_score()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.lives -= 1
        self.scoreboard_score()

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 32, "bold"))
