
#схема Горнера
ER_BASE=3
ER_NUM=4
revnum=''
num=''
base= int(input('Введите систему счисления в которую необходимо перевести число : '))
x = input('Введите десятичной число для перевода в : ')
strx=str(x)
x=int(x)
if base < 2 or base > 9:
    print('Система счисления может быть от 2 до 9')
    exit(ER_BASE)

# for i in range(len(strx)-1,-1,-1):    
#     sx=int(strx[i])
#     if sx >= base:
#         print('Данное число не может существовать в заданной системе')
#         exit(ER_NUM)
while x > 0:
    digital = x%base
    num += str(digital)
    x //= base 
#print(*num)
for i in range(len(num)-1,-1,-1):
    revnum +=num[i]
print('Число в десятичной системе :',revnum)