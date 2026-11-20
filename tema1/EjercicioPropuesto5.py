# E5 ◐ · Media de tres notas con función tipada.
def notas_alumnos(nota1: float, nota2: float, nota3: float,) -> float: # definición de la función con sus variables, se pone -> float: como único valor a dar
    return (nota1 + nota2 + nota3) /3 # operación de la función
print(f"Nota media={notas_alumnos(10, 4, 6)} " ) # no me pide los valores a si que son aleatorios (?) | el print imprime "nota media" y 
# declara los valores de la función en orden