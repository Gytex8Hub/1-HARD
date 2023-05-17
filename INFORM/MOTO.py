from turtle import*
speed(10)

def ruota1(x,y):
    penup()
    goto(x, y)
    pendown()
    pensize(28)
    for i in range(180):
        fd(2.6)
        lt(2)



def ruota2(x, y):
    penup()
    goto(x, y)
    pendown()
    pensize(24)
    for i in range(180):
        fd(2.3)
        lt(2)

def cerchione1():
    pencolor('grey')
    penup()
    goto(-200, -132)
    pendown()
    pensize(8)
    for i in range(180):
        fd(2)
        lt(2)

def cerchione2():
    penup()
    goto(200, -139)
    pendown()
    pensize(8)
    for i in range(180):
        fd(1.8)
        lt(2)

def freno1():
    penup()
    goto(-200, -99)
    pendown()
    pensize(15)
    for i in range(180):
        fd(0.8)
        lt(2)

def freno2():
    penup()
    goto(200, -121)
    pendown()
    pensize(10)
    for i in range(180):
        fd(1.2)
        lt(2)

def raggio1():
    pencolor('blue')
    penup()
    goto(-200, -129)
    pendown()
    pensize(3)
    left(90)
    for i in range(10):
        fd(110)
        backward(55)
        lt(30)
        backward(55)
    fd(110)

def raggio2():
    penup()
    goto(200, -139)
    pendown()
    pensize(3)
    left(60)
    for i in range(10):
        fd(100)
        backward(50)
        lt(30)
        backward(50)
    fd(100)

def telaio():
    pencolor('red')
    pensize(1)
    speed(1)
    penup()
    goto(-110, -100)
    right(30)
    pendown()
    fd(20)
    right(110)
    fd(35)
    left(80)
    fd(30)
    lt(30)
    fd(100)
    left(85)
    fd(15)
    left(55)
    fd(35)
    left(32.5)
    fd(89)
    penup()
    goto(24,-140)
    pendown()
    right(172.5)
    fd(90)
    left(90)
    for i in range(20):
        fd(7.5)
        right(0.8)
    right(74)
    fd(60)
    lt(100)
    fd(10)
    lt(38)
    for i in range(20):
        lt(1)
        fd(4)
    right(60)
    fd(30)
    lt(70)
    fd(25)
    lt(90)
    fd(5)
    lt(90)
    fd(10)
    right(80)
    fd(25)
    right(75)
    fd(20)
    right(55)
    for i in range(75):
        lt(1.2)
        fd(2)
    right(40)
    for i in range(20):
        fd(3.2)
        right(1)
    right(80)
    fd(10)
    for i in range(9):
        lt(10)
        fd(2.3)
    fd(40)
    lt(135)
    fd(40)
    right(130)
    fd(70)
    lt(45)
    fd(40)
    lt(170)
    fd(40)
    right(45)
    fd(75)
    right(30)
    for i in range(20):
        lt(1)
        fd(3)
    right(145)
    fd(50)
    lt(110)
    for i in range(31):
        right(1.8)
        fd(3)

def forcella():
    penup()
    goto(205, -100)
    pendown()
    pencolor('yellow')
    right(132)
    pensize(17)
    fd(200)


print(ruota(-200, -150))
print(ruota2(200, -154))
print(cerchione1())
print(cerchione2())
print(freno1())
print(freno2())
print(raggio1())
print(raggio2())
print(telaio())
print(forcella())

