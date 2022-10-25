#  Первый опыт
# fast comment ctrl+/
msg1="Hello"
msg2="zak"
print(msg1)
print(msg2)
# свойсво sep= (seporate) аналог IFS
# свойство end= по умолчанию равен \n 
print("Результат: ", 6, 15, ".", sep="|")
# объединение вывода
print("Результат: ", 6, 15, ".", sep="", end="")
print(" using option \"end=\"", end="!\n")
print("next line")
# более строгий вывод как и в bash 'в одинарных квч' 
print('only "" \n text \t TAB')
#мат действия 
print("Результат:",5+3)
#остаток от деления
print("Результат:",5%2)
#возвидение в квадрат
print("Результат:",10**2)
# окуругление до целого //
print("Результат:",5/3)
print("Результат:",5//3)