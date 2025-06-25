from tkinter import *
import time
import Ball
import Paddle
import PowerUp



def createPowerUp():
    powerUp = PowerUp.PowerUp(tk, canvas, paddle, ball)
    listOfPowerUps.append(powerUp)
    print("create power up")
    tk.after(5000, createPowerUp)

def makeGameHarder():
    tk.after(5000, paddle.decreaseSize)
    tk.after(5000, ball.increaseSpeed)

    tk.after(5000, makeGameHarder)


def update_game():
    makeGameHarder()
    createPowerUp()




    while True:
        canvas.itemconfig(scoreBoard, text="bounces : {0}".format(ball.ballBounce))

        # powerUp.fallingDown()
        for powerUp in listOfPowerUps:
            if powerUp.isActive:
                powerUp.fallingDown()

        ball.move()
        paddle.move()
        tk.update_idletasks() # This is updating the paddle.
        tk.update()
        #FOR NO BUG
        time.sleep(0.005)

        # FOR BUG
        # time.sleep(0.01)

        if ball.hasBallTouchedGround == True:
            canvas.create_text(250, 200, text="       You lose!\nYou have bounced {0} times.".format(ball.ballBounce), font=("Brownist", 40))
            break



if __name__ == "__main__":
    tk = Tk()
    tk.title('Bounce Game')
    tk.resizable(False, False)
    tk.wm_attributes('-topmost', 1)

    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)


    bg = PhotoImage(file="pingPongBackGround.gif")
    canvas.create_image(250, 200, anchor=CENTER, image=bg)

    canvas.pack()
    tk.update()
    paddle = Paddle.Paddle(tk, canvas, 'blue')
    ball = Ball.Ball(tk, canvas, paddle, 'red')




    listOfPowerUps = []


    scoreBoard = canvas.create_text(375, 100, text="bounces : {0}".format(ball.ballBounce), font=("Brownist", 20))



    # time.sleep(1)
    # update_game()
    # Better version
    tk.after(2000, update_game)




    # print("Program doesn't reach here")
    # make the window stay up after game is over.
    # It's blocking code, you get stuck here
    tk.mainloop()