#множество (set)
s={
    'one',
    'two',
    'three'
}
#s.add(str(input('Add string in set :')))
if "four" in s:
    print(*s)
#словарь (dict)
#содержит ключ + значение
d={
    'one':333,
    'two':555,
    'three':678,
	'four':'kek',
}
d['five']='sick'
for key in d:
    print(key,d[key])