# Escribe mayor(a, b) que devuelva el mayor de dos números, sin usar max().
def mayor (a:int, b:int)-> int:
    if a>b:
        return a
    return b
print(mayor(5, 4))
print(mayor(-2, -7))   
print(mayor(4, 4))  