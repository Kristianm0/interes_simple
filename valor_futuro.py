# @Kristianmartinezcolina
"""📌 ¿Qué es Valor Futuro? -> tema de interes simple
Es el monto que se obtiene despues de un periodo determinado, teniendo en cuenta el capital inicial y los intereses generados durante ese tiempo. 
Lo usamos para evaluar inversiones, prestamos y ahorros.
"""
# --- 📝 Fórmula de VF ---
# VF = P (1 + i * n)
# VF --> Valor Futuro 
# P --> Principal o dinero inicial
# i --> Tasa de interes
# n --> numero de periodo de tiempo (dividir segun el tipo, para dias 365 y meses 12)
""" Ejemplo con Bender de futurama
Si Bender invierte $10,000,000 en un fondo con una tasa de interés simple del 20% anual 
¿cuánto dinero tendrá después de 5 años? 

"""

#Librerias 
import locale 
from decimal import Decimal
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  

#Funcion
def valor_futuro():
    try:
        principal = Decimal(input("Dame el capital: "))
        tasa_interes = Decimal(input("Dame la tasa de interes: ")) / 100
        tipo_tiempo = int(input("""
        Elige un numero segun el tiempo: 
        1. Año
        2. Meses
        3. Dias
        --> """))
        if tipo_tiempo == 1:
            numero_tiempo = Decimal(input("Dame el tiempo en años: "))
        elif tipo_tiempo == 2:
            numero_tiempo = Decimal(input("Dame los meses: ")) / 12
        elif tipo_tiempo == 3: 
            numero_tiempo = Decimal(input("Dame los dias: ")) / 365
        else: 
            print("No es un valor validos: Volve a inicar")
        formula_valor_futuro = principal * (1 + tasa_interes * numero_tiempo)

        resultado = locale.format_string("%.2f", formula_valor_futuro, grouping=True)

        print(resultado)
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

valor_futuro()
# @Kristianmartinezcolina


