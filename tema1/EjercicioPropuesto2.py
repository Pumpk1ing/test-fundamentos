# Rectángulo. Pide base y altura y muestra área y perímetro.
base : float = float(input("Base del rectángulo:"))
altura : float = float(input("Altura del rectángulo:"))
print(f"El area del rectángulo es:", base * altura)
print(f"El perímetro del rectángulo es:", 2*(base*altura))