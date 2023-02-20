def num() ->int:
    pass
    return 5


print(num())

def nogood() ->int:
    import random
    if random.randint(1,2) == 1:
        print("8")
    else:
        print("Hello")
nogood()


def nums(x):
    x[0]=7
    return x
ms=[1,2,3]
print(nums(ms))
