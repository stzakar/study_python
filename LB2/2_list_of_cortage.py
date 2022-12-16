import turtle
lisofc = [(50,60),(50,60),(50,60),(50,60),(50,60),(50,60)]

#---------Method I---------#
# for i in range(len(lisofc)):
#     tm = lisofc[i] # присвоение списка котежей
#     lenght,turn = lisofc[i] #распаковка списка котрежа
#     turtle.forward(lenght)
#     turtle.left(turn)
# turtle.Screen().mainloop()

# #---------Method II--------#
# for prog in lisofc:
#     lenght,turn = prog
#     turtle.forward(lenght)
#     turtle.left(turn)
# turtle.Screen().mainloop()

#---------Method III-------#
for lenght,turn in lisofc:
    turtle.forward(lenght)
    turtle.left(turn)
turtle.Screen().mainloop()