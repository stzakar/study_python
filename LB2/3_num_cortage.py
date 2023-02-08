#listof = ["one","two","three","four","five","six","seven","eleven","eight","ten"]
a=445,33
b=446,55
c="les","mes"
listof = [a,b,c]
for number,element1 in enumerate(listof):
    print(number,*element1)
