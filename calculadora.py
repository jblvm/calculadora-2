def sum(a, b):
    """
    Função responsável por adicionar dois numeros

    Params:
        a :int/float
        b :int/float
    
    Return:
        int
    """
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a/b

def exp(a, b):
    return a * b

def rad(a, b):
    return a**(1/b)

print('Coloque o numero a:')
a = int(input())

print('Coloque o numero b:')
b = int(input())

print(sum(a,b))
print(sub(a,b))
print(div(a,b))
print(exp(a,b))
print(rad(a,b))

print('Coloque o numero c:')
c = int(input())