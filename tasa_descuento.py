# @Kristianmartinezcolina
"""📌 ¿Qué es la tasa de descuento?
Es un porcentaje usa para calcular cuanto vale el dinero presente o hoy que recibiras en un futuro. 
Esta tasa puede ser inflacion, riesgo, costo de oportunidad etc.
"""
""" Ejemplo con McPato
Rico McPato recibe la noticia de que, en 11 meses, le daran $10,000,000.  
Mcpato quiere saber cuánto vale realmente ese dinero hoy si la tasa de descuento es del 15% anual.
"""
# --- 📝 Fórmula de TD ---
# VP = VF(1-d*n)
#-- Datos
# VP = Valor presente
# VF = Valor futuro 
# d = tasa de descuento
# n = numero de periodo de tiempo

# Importamos la librería Decimal 
from decimal import Decimal

# Definimos la función
def f_tasa_decuento(valor_presente, tasa_descuento, numero_tiempo):
    valor_presente = Decimal(valor_presente)
    tasa_descuento = Decimal(tasa_descuento) / 100 
    numero_tiempo = Decimal(tasa_descuento) / 12

    formula_tasa_descuento = valor_presente * (1 - tasa_descuento * numero_tiempo)
    return formula_tasa_descuento

# Llamamos la función con valores de prueba
resultado = f_tasa_decuento(10000000, 15, 11)
# Imprimimos el resultado sin formato
print(resultado)
# Imprimimos el resultado en formato de moneda colombiana
print(f"Valor presente: ${resultado:,.2f} COP")