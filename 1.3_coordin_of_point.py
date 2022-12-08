x=int(input('Enter point X: '))
y=int(input('Enter point Y: '))
print(x,y)
if x > 0:
    if y > 0:
        print('Point in I')
    else:
        print('Point in IV')
if x < 0: #алтернативно можно просто else:
    if y < 0:
        print('Point in III')
    else:
        print('Point in II')
#Логические операции: 
# and or бинарная
# not унарная операция
# xor исключающее или выводит значения не содержащиеся в сравниваемых множествах 
# общие элементы множеств будут исключены
print("-----------second method---------------")
if x > 0 and y > 0:
    print('Point in I')
else:
    if x > 0 and y < 0:
        print('Point in IV')
    else:
        if x < 0 and y < 0:
            print('Point in III')
        else:
            print('Point in II')
print("-----------thrird method---------------")
if x > 0 and y > 0:
    print('Point in I')
elif x > 0 and y < 0:
    print('Point in IV')
elif x < 0 and y < 0:
    print('Point in III')
elif x < 0 and y > 0:
    print('Point in II')
else:
    print("One of the coordinates lies on the coordinate line")