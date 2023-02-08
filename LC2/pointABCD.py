def prt(flg):
    if flg==1:
        print("A")
    if flg==2:
        print("B")
    if flg==3:
        print("C")
    if flg==4:
        print("D")

point=int(input("Enter point : "))
# if point <= 0:
#     flg=1
# if point >0 and point < 5:
#     flg=2
# if point >= 5 and point < 10:
#     flg=3
# if point >= 10:
#     flg=4
if point <= 0:
    num=1
elif point < 5:
    num=2
elif point < 10:
    num=3
else: #point >= 10:
    num=4
#можно бло бы поставить ловушку с выводм невозможности высший пилотаж    
prt(num)