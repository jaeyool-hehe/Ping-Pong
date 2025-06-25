from tkinter import *
import time
import Ball
import Paddle


def update_game():
    tk.after(10000, ball.increaseSpeed)
    tk.after(20000, ball.increaseSpeed)
    tk.after(30000, ball.increaseSpeed)

    while True:
        canvas.itemconfig(scoreBoard, text="bounces : {0}".format(ball.ballBounce))
        ball.move()
        paddle.move()
        tk.update_idletasks() # This is updating the paddle.
        tk.update()
        time.sleep(0.01)
        if ball.hasBallTouchedGround == True:
            canvas.create_text(250, 250, text="You lose!", font=("Brownist", 40))
            break



if __name__ == "__main__":
    tk = Tk()
    tk.title('Bounce Game')
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()
    paddle = Paddle.Paddle(canvas, 'blue')
    ball = Ball.Ball(canvas, paddle, 'red')
    scoreBoard = canvas.create_text(375, 100, text="bounces : {0}".format(ball.ballBounce), font=("Brownist", 20))

    # Better version of this
    # time.sleep(1)
    # update_game()
    tk.after(2000, update_game)


    # print("Program doesn't reach here")
    # make the window stay up after game is over.
    # It's blocking code, you get stuck here
    tk.mainloop()