import turtle
t=turtle.Pen()
irange=int(input('inserici il numero di scalini'))
l=20
for i in range(irange):
    t.left(90)
    t.forward(l)
    t.right(90)
    t.forward(l)

t.right(90)
t.forward(l*irange)
t.right(90)
t.forward(l*irange)


