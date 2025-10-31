from turtle import * 
title("Avengers Logo")
bgcolor('black')
setup(width=650, height=670)
speed(10)
pensize(10)
penup()

def print_circle():
    # bhahar ka gola
    setposition(0, -280)
    pendown()
    begin_fill()
    color('blue')
    pencolor('red')
    circle(300)
    end_fill()
    penup()

def print_circle2():
    # andar ka gola
    pensize(2)
    setposition(0, -230)
    pendown()
    begin_fill()
    color('black')
    circle(250)
    end_fill()
    penup()

def print_A():
    # print 'A'
    setposition(30, -110)    
    pendown()
    begin_fill()
    color('blue')
    pensize(10)
    pencolor('red')
    forward(23)
    backward(123)
    left(60)
    backward(220)
    right(60)
    backward(100)
    right(117)
    backward(710)
    right(63)
    backward(110)
    right(90)
    backward(510)
    right(90)
    backward(100)
    right(90)
    backward(70)
    end_fill()
    penup()

def print_triangle():
    # 2d jaisa dikhne k liye 'A' 
    # me triangle shape
    pensize(10)    
    setposition(53, -40)
    pendown()
    begin_fill()
    color('black')
    pencolor('red')
    right(90)
    forward(100)
    right(115)
    forward(250)
    right(157)
    forward(227)
    end_fill()

def print_arrow():
    # 'A' ke andar ka arrow
    backward(80)    
    left(42)
    forward(147)
    right(83)
    forward(140)

print_circle()    
print_circle2()
print_A()
print_triangle()
print_arrow()

hideturtle()
done()