import time


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.xSpeed = 0
        self.canvas_width = self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def move(self):
        self.canvas.move(self.id, self.xSpeed, 0)

        # when paddle hits the left and right wall, stop the paddle
        paddleCoordinate = self.canvas.coords(self.id)
        if paddleCoordinate[0] <= 0 or paddleCoordinate[2] >= self.canvas_width:
            self.xSpeed = 0
    def turn_left(self, evt):
        # when paddle hits left wall, you can't move it to the left
        paddleCoordinate = self.canvas.coords(self.id)
        if paddleCoordinate[0] > 0:
            self.xSpeed = -3

    def turn_right(self, evt):
        # when paddle hits right wall, you can't move it to the right
        paddleCoordinate = self.canvas.coords(self.id)
        if paddleCoordinate[2] < self.canvas_width:
            self.xSpeed = 3

