from turtle import Turtle

class Player(Turtle):
    def __init__(self, position, color):
        # self.player_racket1 = [(-270,0), (-270,20), (-270,40), (-270,60)]
        # self.player_racket2 = [(270,0), (270,20), (270,40), (270,60)]
        # self.list_pl1 = []
        # self.list_pl2 = []
        super().__init__()
        self.penup()
        self.goto(position)
        self.color(color)
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.shape("square")

        # self.player1()
        # self.player2()

    # def player1(self):
    #     for i in self.player_racket1:
    #         player1 = Turtle(shape="square")
    #         player1.color("blue")
    #         player1.penup()
    #         player1.goto(i)
    #         self.list_pl1.append(player1)
            

    # def player2(self):
    #     for i in self.player_racket2:
    #         player2 = Turtle(shape="square")
    #         player2.color("red")
    #         player2.penup()
    #         player2.goto(i)
    #         self.list_pl2.append(player2)

    def move_player_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor()+20)
        #if self.list_pl1[-1].ycor() != 280:
            # for i in range(len(self.list_pl1) - 1):
            #     self.list_pl1[i].goto(self.list_pl1[i+1].pos())
            
            # self.list_pl1[-1].setheading(90)
            # self.list_pl1[-1].forward(20)

    def move_player_dowen(self):
        if self.ycor() > -230:
             self.goto(self.xcor(), self.ycor()-20)
        #  if self.list_pl1[0].ycor() != -280:
        #     c = len(self.list_pl1) - 1
        #     for _ in range(len(self.list_pl1) - 1):
        #         self.list_pl1[c].goto(self.list_pl1[c-1].pos())
        #         c -= 1

        #     self.list_pl1[0].setheading(270)
        #     self.list_pl1[0].forward(20)


    # def move_player2_up(self):
    #     if self.list_pl2[-1].ycor() != 280:
    #         for i in range(len(self.list_pl2) - 1):
    #             self.list_pl2[i].goto(self.list_pl2[i+1].pos())

    #         self.list_pl2[-1].setheading(90)
    #         self.list_pl2[-1].forward(20)


    # def move_player2_dowen(self):
    #     if self.list_pl2[0].ycor() != -280:
    #         c = len(self.list_pl2) - 1
    #         for _ in range(len(self.list_pl2) - 1):
    #             self.list_pl2[c].goto(self.list_pl2[c-1].pos())
    #             c -= 1

    #         self.list_pl2[0].setheading(270)
    #         self.list_pl2[0].forward(20)

    
    

    


