segundos : int = int(input("Tiempo en segundos: "))
horas: int = segundos / 3600 
minutos: int = (segundos%3600) / 60
segundos2: int = segundos % 60
print(f"Horas:",horas,"Minutos:",minutos,"Segundos:",segundos2)
