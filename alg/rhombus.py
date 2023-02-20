
# def rhomb(stdiam:int) ->str:
#     ifs = ""
#     diam = stdiam
    
#     #diam=int(input('Enter a diameter of rhombus: '))
   




#     for x in range(diam,0,-1) :
#     #Стартовые значения 
#         msg = ' '

#     #проверка конца строки
#         if x == 1: 
#             ifs = "\n"
    
#     #пеать строки
#         if x == diam or x == 1 :
#             msg = "*"
#         print(msg , end=ifs)



# rhomb(7)

# print('___*')
# print('__***')
# print('_*****')
# print('*******')
# print('_*****')
# print('__***')
# print('___*')


# print('__*')
# print('_***')
# print('*****')
# print('_***')
# print('__*')
# print("*"*2+" "*3)

while True:
    diam = int(input('Enter diametr :'))
   
#diam = 11
    s=round(diam/2)
    z=1
    for i in range(1,diam,1):
        if z > diam:
            break
        print(" "*s+"*"*z)
        z=z+2
        s=s-1
    
    z=diam-2
    s=1
    for i in range(1,diam,1):
        print(" "*s+"*"*z)
        s=s+1
        z=z-2
        if z < 0:
            break

