# @Kristianmartinezcolina
"""📌 Ejercicio de interes simple -> ¿Como calcular el tiempo en una inversion?
Vamos Calcular el tiempo requerido para que una inversión genere ciertos intereses usando la fórmula del interés simple.
"""

""" Ejemplo con un Mr. big de Zootopia
 Mr. big de Zootopia deposita $8,000,000 en un banco con una tasa de interés del 10% anual.

Pregunta:
¿Cuánto tiempo debe transcurrir para que la inversión genere $2,000,000 en intereses?
"""
# --- Fórmula del Tiempo en Interés Simple ---
# n = I / (P * i)

"""Datos
# I -> Interés generado = $2,000,000
# P -> Capital inicial = $8,000,000
# i -> Tasa de interés anual en decimal(se divide entre 100) = 10% = 0.10
"""

from decimal import Decimal 

def calcular_tiempo():
    try: 
        interes_generado = Decimal(input("Dame los interes generados: "))
        principal = Decimal(input("Dame el capital: "))
        tasa_interes = Decimal(input("Dame la tasa de interes: ")) / 100

        formula_calcular_tiempo = interes_generado / (principal * tasa_interes)

        años = int(formula_calcular_tiempo)
        meses = round((formula_calcular_tiempo - años)*12)

        resultado = f"{años} años y {meses} meses"
        print("Tiempo necesario:", resultado)

    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

calcular_tiempo()