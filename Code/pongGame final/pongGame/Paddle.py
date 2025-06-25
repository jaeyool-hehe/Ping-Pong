import time


class Paddle:
    def __init__(self, tk, canvas, color):
        self.tk = tk
        self.canvas = canvas
        self.shape = canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.move(self.shape, 200, 300)
        self.xSpeed = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop)


    def move(self):
        self.canvas.move(self.shape, self.xSpeed, 0)

        # when paddle hits the left and right wall, stop the paddle
        paddleCoordinate = self.canvas.coords(self.shape)
        if paddleCoordinate[0] <= 0 or paddleCoordinate[2] >= self.canvas_width:
            self.xSpeed = 0

    def turn_left(self, evt):
        # print("Left key pressed")
        # when paddle hits left wall, you can't move it to the left
        paddleCoordinate = self.canvas.coords(self.shape)
        if paddleCoordinate[0] > 0:
            self.xSpeed = -3
            # self.tk.after(1, self.stop)

    def turn_right(self, evt):
        # print("Right key pressed")

        # when paddle hits right wall, you can't move it to the right
        paddleCoordinate = self.canvas.coords(self.shape)
        if paddleCoordinate[2] < self.canvas_width:
            self.xSpeed = 3
            # self.tk.after(1, self.stop)


    def stop(self, evt):
        self.xSpeed = 0

    def decreaseSize(self):
        topLeftX, topLeftY, bottomRightX, bottomRightY = self.canvas.coords(self.shape)
        bottomRightX *= 0.95
        topLeftX *= 1.05
        self.canvas.coords(self.shape, topLeftX, topLeftY, bottomRightX, bottomRightY)