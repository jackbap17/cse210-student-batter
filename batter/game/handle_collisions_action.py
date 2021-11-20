import random
import sys
#from batter.game import point
from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class HandleCollisionsAction(Action):
   
   
    def execute(self, cast):
        paddle = cast["paddle"][0]
        paddle_position = paddle.get_position()
        ball = cast["ball"][0]
        bricks = cast["bricks"]
       
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()) and brick.get_text() != ' ':    
                brick.set_text(' ')
                ball.set_velocity(ball.get_velocity().reverse())
        
        if ball.get_position().get_y() == 2 or ball.get_position().get_y() == 1 :
             ball.set_velocity(Point(1,random.randint(-2,2)))

        if ball.get_position().get_x() == 2 or ball.get_position().get_x() == 1:
            y = ball.get_velocity().get_y()
            ball.set_velocity(Point(1,y))
        
        if ball.get_position().get_x() == 78 or ball.get_position().get_x() == 79:
            y = ball.get_velocity().get_y()
            ball.set_velocity(Point(-1,y))          
            
        for x in range(1,14):        
            if paddle.get_position().add(Point(-2,0)).add(Point(x,0)).equals(ball.get_position()):
                 ball.set_velocity(Point(random.randint(-2,2),-1))

            if ball.get_position().get_y() == 19:
                sys.exit()

