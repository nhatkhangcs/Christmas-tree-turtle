import turtle

# sleep

# TELA 
width = 800  # Wider screen for a larger tree
height = 600
S = turtle.Screen()
S.setup(width, height)
S.title('FELIZ NATAL !')
# Increased dimensions for a bigger tree


T = turtle.Pen()
T.speed(1)

import time
time.sleep(5)

# Topo da arvore
T.up()
T.setposition(-60,100)
T.down()
T.fillcolor('green')
T.begin_fill()
T.fd(120)
T.lt(130)
T.fd(95)
T.lt(100)
T.fd(95)
T.end_fill()

# Meio da arvore
T.setx(-35)
T.fillcolor('green')
T.begin_fill()
T.fd(100)
T.lt(130)
T.fd(200)
T.lt(130)
T.fd(100)
T.end_fill()

# 
T.up()
T.setposition(-45,24)
T.down()
T.fillcolor('green')
T.begin_fill()
T.lt(100)
T.fd(130)
T.lt(130)
T.fd(260)
T.lt(130)
T.fd(130)
T.end_fill()

# Tronco
T.up()
T.setposition(-30,-75)
T.down()
T.fillcolor('brown')
T.begin_fill()
T.lt(140)
T.fd(50)
T.lt(90)
T.fd(60)
T.lt(90)
T.fd(50)
T.end_fill()

# Estrela
T.up()
T.setposition(-30,196)
T.rt(90)
T.down()
T.color('yellow')
T.begin_fill()

for i in range(5):
     T.fd(60)
     T.rt(144)
     T.color('yellow')
T.end_fill()
T.hideturtle()


# pisca pisca 
colors = ['red','yellow','cyan']

T1 = turtle.Pen()
T2 = turtle.Pen()
T3 = turtle.Pen()
T4 = turtle.Pen()
T5 = turtle.Pen()
T6 = turtle.Pen()
T7 = turtle.Pen()
T8 = turtle.Pen()
T9 = turtle.Pen()

T1.up()
T1.setposition(0,-20)
T1.down()
T1.hideturtle()

T2.up()
T2.setposition(0,60)
T2.down()
T2.hideturtle()

T3.up()
T3.setposition(0,130)
T3.down()
T3.hideturtle()

T4.up()
T4.setposition(-60,100)
T4.down()
T4.hideturtle()

T5.up()
T5.setposition(60,100)
T5.down()
T5.hideturtle()

T6.up()
T6.setposition(130,-80)
T6.down()
T6.hideturtle()

T7.up()
T7.setposition(-100,25)
T7.down()
T7.hideturtle()

T8.up()
T8.setposition(100,25)
T8.down()
T8.hideturtle()

T9.up()
T9.setposition(-130,-80)
T9.down()
T9.hideturtle()


# Flashing light
m = 0
while True:
    T1.dot(20,colors[m%3]) 
    T2.dot(20,colors[(m+1)%3]) #1,2,0,1,2,0,1,2,0,...
    T3.dot(20,colors[(m+3)%3]) #2,0,1,2,0,1,2,0,1,...
    T4.dot(20,colors[(m+2)%3])
    T5.dot(20,colors[(m+1)%3])
    T6.dot(20,colors[(m+4)%3])
    T7.dot(20,colors[(m+2)%3])
    T8.dot(20,colors[(m+3)%3])
    T9.dot(20,colors[(m+2)%3])
    m=m+1