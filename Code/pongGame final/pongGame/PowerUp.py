import random

# type can be one of:
# "Bigger Paddle"
# "Slow Motion"
# "Plus Ten Bounces"
# "Double Score"




class PowerUp:
    def __init__(self, tk, canvas, paddle, ball):
        powerUpTypes = ["Bigger Paddle", "Plus Ten Bounces"]
        powerUpColor = ["red2", "green"]


        randomIndex = random.randint(0, len(powerUpTypes) - 1)
        self.type = powerUpTypes[randomIndex]
        self.color = powerUpColor[randomIndex]

        # For testing purposes
        self.type = powerUpTypes[0]
        self.color = powerUpColor[0]

        self.tk = tk
        self.canvas = canvas
        self.canvas_height = self.canvas.winfo_height()

        self.paddle = paddle
        self.ball = ball

        self.shape = canvas.create_rectangle(0, 0, 40, 40, fill=self.color)

        startLocation = [10, 50, 150, 200, 250, 300, 350, 400]
        self.xStartingLocation = random.choice(startLocation)

        # TODO: the starting location should be (self.xStartingLocation, 0)
        self.canvas.move(self.shape, self.xStartingLocation, 0)
        # self.canvas.move(self.shape, 245, 0)

        self.ySpeed = 3

        self.isActive = True


    def checkPowerUpHitPaddle(self, powerUp_pos):
        paddle_pos = self.canvas.coords(self.paddle.shape)
        # the power up is within the paddle's width
        if paddle_pos[0] <= powerUp_pos[2] and powerUp_pos[0] <= paddle_pos[2]:
            # the power up is within the paddle's width AND on top of the paddle
            # which means power up will hit the paddle
            if powerUp_pos[3] >= paddle_pos[1]:
                return True
            return False

# return False when powerUp is unavailable
# otherwise, return None
    def fallingDown(self):
        if self.isActive:
            self.canvas.move(self.shape, 0, self.ySpeed)
            pos = self.canvas.coords(self.shape)
            # print(pos)

            # the powerUp will disappear after hitting the bottom
            # greater the y-axis, it means it's more at the bottom
            if pos[3] >= self.canvas_height:
                # power up disappear code
                self.destroy()
            # powerUp disappears once it hits the paddle
            elif self.checkPowerUpHitPaddle(pos) == True:
                self.applyPowerUps()
                # power up disappear code
                self.destroy()


    def destroy(self):
        # delete the rectangle shape on the canvas
        self.canvas.delete(self.shape)
        self.isActive = False

    def applyPowerUps(self):
        if self.type == "Bigger Paddle":
            print("bigger paddle")
            print(self.paddle)
            paddlePos = self.canvas.coords(self.paddle.shape)
            paddlePos[0] *= 0.9
            paddlePos[2] *= 1.1
            self.canvas.coords(self.paddle.shape, paddlePos[0], paddlePos[1], paddlePos[2], paddlePos[3])

        elif self.type == "Plus Ten Bounces":
            print("plus ten bounce")
            self.ball.ballBounce += 10

