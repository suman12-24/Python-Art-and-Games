from turtle import *
import colorsys
bgcolor('black')
pensize(4)
h = 0.5
m = 5
tracer(50)
width(2)
up()
goto(-290,0)
down()

for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.005
    for j in range(5):
        fd(130)
        lt(5)
    lt(65)
    circle(330)
    lt(65)
done()