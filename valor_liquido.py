# @Kristianmartinezcolina
"""📌 ¿Qué es Valor liquido? -> tema de interes simple
Es el dinero realque recibes despues de aplicar descuentos o impuestos a un monto original.
"""
# --- 📝 Fórmula de VL ---
# VL = VN (1 - d * n)
# VN --> Valor nominal o monto original
# d --> Tasa de descuento en decimales (porcentaje dividido entre 100)
# n --> numero de periodo de tiempo (dividir segun el tipo, para dias 365 y meses 12)
""" Ejemplo con Sr. Burns de los Simpson
"El Sr. Burns invierte mil millones (1.000.000.000) de pesos en un fondo que le ofrece un interés simple anual del 9%. 

Pregunta:
¿Cuál será el valor líquido de su inversión después de 5 años?"
"""

#Librerias
import locale
from decimal import Decimal
#Confi numeros de latam
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  

#Funcion pidiendo valores en consola y eligiendo tiempo
def valor_liquido():
    try:
        valor_nominal = Decimal(input("Dame el Valor nominal: "))
        tasa_descuento = Decimal(input("Dame la tasa de interes: ")) / 100
        tipo_tiempo = float(input("""
        Elige un numero segun el tiempo: 
        1. Año
        2. Meses
        3. Dias"""))
        if tipo_tiempo == 1:
            numero_tiempo = Decimal(input("Dame el tiempo en años: "))
        elif tipo_tiempo == 2:
            numero_tiempo = Decimal(input("Dame los meses: ")) / 12
        elif tipo_tiempo == 3: 
            numero_tiempo = Decimal(input("Dame los dias: ")) / 365
        else: 
            print("No es un valor validos: Volve a inicar")
        formula_valor_liquido = valor_nominal * (1 - tasa_descuento * numero_tiempo)

        resultado = locale.format_string("%.2f", formula_valor_liquido, grouping=True)

        print(resultado)

    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")

valor_liquido()

# @Kristianmartinezcolina