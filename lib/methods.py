def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise NameError("Cannot divide by zero")
    return a/b

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    greater = max(a,b)
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

def hcf(a, b):
    if a == 0 or b == 0:
        return 0
    smaller = min(a,b)
    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf