t=1,2,3,4,5
print(type(t))
print(*t,sep='8=>')
a,b,*rest=t
for i in a,b,rest:
    print(i)

def hello_n(name:str,n:int):
    for i in range(n):
        print('привет',name)
#hello_n(input('Укажи имя '),int(input('сколько раз ')))
#Вызов через кортеж:
vizov = 'Ivan',3
hello_n(*vizov)
z = range(1,5)
print(*z)

m = [1,2,3]
print(type(m))