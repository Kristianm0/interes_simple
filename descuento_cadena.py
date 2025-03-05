# @Kristianmartinezcolina
"""📌 ¿Qué es Descuento en Cadena?
Se usa cuando un mismo valor futuro (precio original) recibe dos o más descuentos consecutivos. 
No se suman directamente los descuentos, sino que se aplican en secuencia, recalculando el precio después de cada descuento.
"""
""" Ejemplo con Benson de un show más
Benson ofrece un descuento en cadena en la compra de un boleto de entrada al parque ($50.000):

1° descuento → 10%
2° descuento → 20% sobre el precio ya rebajado
3° descuento → 30% sobre el precio final

Pregunta:
Si alguien recibe todos los descuentos en cadena, ¿cuánto terminará pagando por su boleto?
"""
# --- 📝 Fórmula de DC ---
# VF = P x (1 - d1) x (1 - d2) x (1 - d3)...
"""Datos
#VF -> Valor final despues de descuento
# P -> Precio
# d1, d2, d3... -> Descuentos en decimales (porcentaje dividido entre 100)"""

#Importamos decimal
from decimal import Decimal
#Funcion donde le pide los valores por consola
def descuento_cadena():
    precio = Decimal(input("Dame el precio inicial: "))
    d1 = Decimal(input("Descuento #1: ")) / 100
    d2 = Decimal(input("Descuento #2: ")) / 100
    d3 = Decimal(input("Descuento #3: ")) / 100

    formula_descuento_cadena = precio * (1 - d1) * (1 - d2) * (1 - d3)

    resultado_d_c = f"{formula_descuento_cadena:,.2f} COP"

    return f"Precio final aplicando el descuento en cadena: {resultado_d_c}"

print(descuento_cadena())