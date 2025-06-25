import time
import random

class Ball:
    def __init__(self, tk, canvas, paddle, color):

        self.tk = tk
        self.canvas = canvas
        self.paddle = paddle
        self.shape = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.shape, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.xSpeed = random.choice(starts) * 0.5
        self.ySpeed = -3 * 0.5

        # For testing
        # self.ySpeed = 0

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hasBallTouchedGround = False
        self.ballBounce = 0
    def checkIfBallHitPaddle(self, ball_pos):
        paddle_pos = self.canvas.coords(self.paddle.shape)
        # the ball is within the paddle's width
        if paddle_pos[0] <= ball_pos[2] and ball_pos[0] <= paddle_pos[2]:
            # the ball is within the paddle's width AND on top of the paddle
            # which means ball hit the paddle
            if ball_pos[3] >= paddle_pos[1]:
                return True
            return False


    def move(self):
        self.canvas.move(self.shape, self.xSpeed, self.ySpeed)
        pos = self.canvas.coords(self.shape)

        # ball bounces back when it hits the top wall
        if pos[1] <= 0:
            self.ySpeed = self.ySpeed * -1
        # the ball DOES NOT bounce back after hitting bottom wall
        # greater the y-axis, it means it's more at the bottom
        if pos[3] >= self.canvas_height:
            self.hasBallTouchedGround = True

        # ball bounce back when it hits the paddle
        # and increment ballBounce
        if self.checkIfBallHitPaddle(pos) == True:
            self.ballBounce += 1
            self.ySpeed = self.ySpeed * -1

        # ball bounces back when it hits the left or right wall
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.xSpeed = self.xSpeed * -1

    def increaseSpeed(self):
        self.xSpeed *= 1.2
        self.ySpeed *= 1.2
        self.warningText = self.canvas.create_text(250, 200, text="!! Increasing speed !!", font=("Brownist", 40))
        self.tk.after(2000, self.deleteWarningText)
    def deleteWarningText(self):
        self.canvas.delete(self.warningText)

