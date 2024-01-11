from turtle import Turtle

ALIGNMNET = "center"
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"score: {self.score}", False, ALIGNMNET, FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", False, ALIGNMNET, FONT)
        self.goto(0,-20)
        # self.write(f"Your new highscore is {highscore}", False, ALIGNMNET, FONT)

    # def highscore(self):
    #     highscore = 0
    #     if self.score > highscore:
    #         highscore = self.score

    def point(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score}", False, ALIGNMNET, FONT)