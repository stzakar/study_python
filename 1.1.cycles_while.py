# цикл с предусловием while
# while усолвие:
#     оператор1
#     if что то:
#           break (минуя else выйти из цикла)     
#     оператор3
# else:
#     после всех 
#     итерация
x=int(input("Enter the number: "))
#y=x
while x>0:
    y=x
    while y>0:
        y-=1
        print("Переменная Y=",y)
    x-=1
    print("X равен =",x)
    if x==0:
        print("stop")
    else:
        print("!")
for x in 1,5,2,4,3:
    print (x**2)
#генератор арифметической прогрессии range (start,stop,step)1
print("генератор арифметической прогрессии")
for i in range(1,11,2):
    print(i)
#функция len сама вычислит длинну массива 
arr=['One','Two','Three','Four','Five','Six']
for j in range(len(arr)):
    print(arr[j])
    print(type(arr))
    