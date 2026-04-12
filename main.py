from turtle import Screen
from score import Score
from player import Player
from ball import Ball
import time

window = Screen()
window.setup(600,600)
window.bgcolor("black")
window.title("Ping Pong Game")
window.tracer(0)


player1 = Player((-270,0), "blue")
player2 = Player((270,0), "red")
the_ball = Ball()
the_score = Score()

window.listen()
window.onkeypress(player2.move_player_up,"Up")
window.onkeypress(player2.move_player_dowen,"Down")
window.onkeypress(player1.move_player_up,"w")
window.onkeypress(player1.move_player_dowen,"s")

defuelt_time = 0.1
game_on = True
while game_on:
    the_ball.goto(the_ball.xcor() + the_ball.x_move , the_ball.ycor() + the_ball.y_move)

    if the_ball.ycor() >= 280 or the_ball.ycor() <= -280:
        the_ball.y_move *= -1

    if the_ball.xcor() >= 250 and the_ball.distance(player2) <= 60 or the_ball.xcor() <= -250 and the_ball.distance(player1) <= 60:
        the_ball.x_move *= -1
        defuelt_time -= 0.01 
        

    if the_ball.xcor() > 280:
        the_ball.goto(player1.xcor()+20, player1.ycor())
        the_score.increase_score1()
        defuelt_time = 0.1
        

    if the_ball.xcor() < -280:
        the_ball.goto(player2.xcor()-20, player2.ycor())
        the_score.increase_score2()
        defuelt_time = 0.1

    if the_score.score_1 == 10:
        the_score.goto(0,0)
        the_score.write("Player One Winner",font=("Arial",30,"normal"),align="center")
        game_on = False

    if the_score.score_2 == 10:
        the_score.goto(0,0)
        the_score.write("Player Two Winner",font=("Arial",30,"normal"),align="center")
        game_on = False

    window.update()
    time.sleep(defuelt_time)

window.exitonclick()