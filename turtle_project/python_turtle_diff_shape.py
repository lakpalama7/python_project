from turtle import Turtle, Screen
import random

jimmy_turtile=Turtle()
jimmy_turtile.shape('turtle')
jimmy_turtile.color('red')

colorlist=['red','green','blue','purple','black','orange','yellow','brown']

# for i in range(3,11):
#     for j in range(i):
#         jimmy_turtile.color(colorlist[i])
#         jimmy_turtile.forward(50)
#         jimmy_turtile.right(360/i)
        
def draw_shape(size):
    draw_angle=360/size
    for _ in range(size):
        jimmy_turtile.forward(100)
        jimmy_turtile.right(draw_angle)


for size in range(3, 11):
    pencolor=random.choice(colorlist)
    jimmy_turtile.color(pencolor)
    draw_shape(size)


screen=Screen()
screen.exitonclick()