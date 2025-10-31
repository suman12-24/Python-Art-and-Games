#drawing maa durga using python turtle
from turtle import*
title("Tej.programmingkakeeda.com")
bgcolor("white")

def pos(x,y):
    penup()
    goto(x,y)
    pendown()

pos(0,200)
begin_fill()
circle(40)
color("red")
end_fill()

#left eyebrow
color("black")
pos(-30,200)
begin_fill()
right(45)
for i in range(20):
    left(3)
    back(10)
for i in range(10):
    right(3)
    back(10)
right(18)    
for i in range(13):
    left(3)
    forward(10)
for i in range(20):
    right(2)    
    forward(10)
end_fill()    

# right eyebrow
left(80)
pos(30,200)
begin_fill()
for i in range(20):
    right(3)
    forward(10)
for i in range(10):
    left(3)    
    forward(10)
left(18)    
for i in range(13):
    right(3)
    back(10)
for i in range(20):
    left(2)    
    back(10)
end_fill()    

# right eye
pos(40,150)
pensize(15)
left(10)
for i in range(20):
    right(3)
    forward(10)
for i in range(10):    
    left(3)
    forward(5)
right(3)    
for i in range(10):
    left(3)
    back(5)
for i in range(20):
    right(3)    
    back(10)
pensize(1)    
pos(130,130)
begin_fill()
circle(40)
end_fill()
color('white')
begin_fill()
pos(115,175)
circle(10)
end_fill()

# left eye
pos(-40,150)
color('black')
pensize(15)
right(25)
for i in range(20):
    left(3)
    back(10)
for i in range(10):
    right(3)    
    back(5)
left(3)    
for i in range(10):
    right(3)
    forward(5)
for i in range(20):
    left(3)    
    forward(10)
pensize(1)    
pos(-130,130)
begin_fill()
circle(40)
end_fill()
color('white')
begin_fill()
pos(-155,175)
circle(10)
end_fill()

# nose
color('black')
pos(-60,10)
right(70)
for i in range(5,12):
    pensize(i)
    left(7)
    forward(10)
for i in range(12,5,-1):
    pensize(i)    
    left(7)
    forward(10)

# lips  
color("red")  
begin_fill()
pos(-130,-90)
pensize(1)
begin_fill()
right(60)
for i in range(3):
    left(3)
    forward(5)
for i in range(10):
    left(4)    
    forward(6)
for i in range(10):
    right(10)    
    forward(7)
left(135) 
for i in range(10):
    right(10)   
    forward(7)
right(2)    
for i in range(10):
    left(4)
    forward(6)
for i in range(3):
    left(3)
    forward(5)
right(160)    
for i in range(12):
    right(3)
    forward(7.2)
left(44)    
for i in range(15):
    right(5.5)
    forward(7)
left(44)    
for i in range(12):
    right(3)
    forward(7)
end_fill()    

# lower lip
begin_fill()   
left(175)
for i in range(14):
    left(2)
    forward(5)
right(45)    
for i in range(14):
    left(7)
    forward(10)
right(45)    
for i in range(14):
    left(3)
    forward(5)
right(185)    
for i in range(7):
    left(3)
    forward(10)
right(0.6)    
for i in range(18):
    right(6)
    forward(10)
right(8)    
for i in range(7):
    left(3)
    forward(10)
end_fill()    

# nose ring 
pensize(12)
color("goldenrod")
pos(30,0)
left(120)
for i in range(47):
    right(7)
    back(10)

hideturtle()    
done()