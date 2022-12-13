#apt install python3-tk
#https://docs.python.org/3/library/turtle.html
import turtle
def trdv():
    turtle.color('green', 'red') # цвет линии , цыет заливки
    turtle.shapesize(2)    #Размер скина
    turtle.shape('turtle') #скин
    turtle
    for i in range(6):
        turtle.begin_fill() # Начало заливки
        for i in range(3):
            turtle.fd(50) #fd==forward
            turtle.left(360/3)
        turtle.forward(50)
        turtle.right(360/6)
        turtle.end_fill() # Конец заливки
    turtle.hideturtle()
    turtle.Screen().mainloop()
    #turtle.done()
    #позволяет не закрывать окно после выполнения
trdv()
#turtle.goto(200,200)
# trdv()
