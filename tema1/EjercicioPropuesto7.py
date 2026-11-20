#linea_ticket(producto: str, unidades: int, precio: float) -> str 
# devuelve una línea como Camisa 2 x 19.90 = 39.80 €: 
# el producto a la izquierda en 12 huecos, las unidades a la derecha en 3, el precio en 6 con 2 decimales y el importe en 8.
#Una sola f-string con cuatro campos: :<12, :>3, :>6.2f y :>8.2f.

def linea_ticket(producto: str, unidades: int, precio: float) -> str:
    print(f"{producto:<12}{unidades:>3} x{precio:>6.2f}={unidades*precio:>8.2f}€")
linea_ticket("Camisa",2,19.90)