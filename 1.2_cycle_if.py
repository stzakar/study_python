# x //= 2 == x=x//2  x %= 2 (остаток по модулю 2)
# x +=1 (инкрементация) x -=1 (декриментация)
# x *= 2 x /= 2
#style of coding PEP8
# https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html
x = 10
while True:
    x -= 1
    if x < 0 :
        break
    print(x)
print("the end")
#------
x = 9
while x > 0:
    x -= 1
    print(x)
print("the end")

for x in 5,3,7:
    print(x**2)

 #range(start,stop,step)
for x in range(1,50,1):
    eol=""
    if x == 49:
        eol="\n"
    print(x, end=eol)