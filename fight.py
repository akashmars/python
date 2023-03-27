import turtle
import sys
import time

wn = turtle.Screen()
wn.title("Fight by CosmicPig")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
        
# Player
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.color("red")
player_a.penup()
player_a.goto(-350, 0)
player_a.shapesize(stretch_wid=1, stretch_len=1)



# Functions
def player_a_up():
    player_a.color("yellow")
    y = player_a.ycor()
    y += 20
    player_a.sety(y)

def player_a_down():
    player_a.color("orange")
    y = player_a.ycor()
    y -= 20
    player_a.sety(y)

def player_a_left():
    player_a.color("light blue")
    x = player_a.xcor()
    x -= 20
    player_a.setx(x)

def player_a_right():
    player_a.color("light green")
    x = player_a.xcor()
    x += 20
    player_a.setx(x)

def player_a_shoot():
    projectile = turtle.Turtle()
    projectile.goto(player_a.xcor(), player_a.ycor())
    projectile.speed(2)
    projectile.shape("square")
    projectile.color("white")
    projectile.shapesize(stretch_wid=0.75, stretch_len=0.75)
    projectile.penup() 
    while projectile.ycor() <= 290:
        projectile.dy = 10
        projectile.sety(projectile.ycor() + projectile.dy)
        time.sleep(0.05)
        projectile.move(25)  
# Listen
wn.listen()
wn.onkey(player_a_up, "w")
wn.onkey(player_a_down, "s")
wn.onkey(player_a_left, "a")
wn.onkey(player_a_right, "d")
wn.onkey(player_a_shoot, "space")

# Test
while True:
    wn.update()
    
