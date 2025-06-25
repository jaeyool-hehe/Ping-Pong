import time
import random


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        self.xSpeed = random.choice(starts) * 0.5
        self.ySpeed = -3 * 0.5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hasBallTouchedGround = False
        self.ballBounce = 0
    def hit_paddle(self, ball_pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        # the ball is within the paddle's width
        if paddle_pos[0] <= ball_pos[2]  and ball_pos[0] <= paddle_pos[2]:
            # the ball is within the paddle's width AND on top of the paddle
            # which means ball hit the paddle
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                # increment ballBounce
                self.ballBounce += 1
                return True
            return False
    def move(self):
        self.canvas.move(self.id, self.xSpeed, self.ySpeed)
        pos = self.canvas.coords(self.id)

        # ball bounces back when it hits the top wall
        if pos[1] <= 0:
            self.ySpeed = self.ySpeed * -1
        # the ball DOES NOT bounce back after hitting bottom wall
        if pos[3] >= self.canvas_height:
            self.hasBallTouchedGround = True

        # ball bounce back when it hits the paddle
        if self.hit_paddle(pos) == True:
            self.ySpeed = self.ySpeed * -1

        # ball bounces back when it hits the left or right wall
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.xSpeed = self.xSpeed * -1

    def increaseSpeed(self):
        self.xSpeed *= 1.2
        self.ySpeed *= 1.2
        print("increasing speed.")


