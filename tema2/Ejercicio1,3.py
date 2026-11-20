#1.3. Escribe la función más pequeña posible que evite repetir el cálculo del IVA en un programa que factura tres artículos.

def cálculo_artículos(art1:float,art2:float,art3:float,iva:int=21) -> tuple[float,float,float]:
    return