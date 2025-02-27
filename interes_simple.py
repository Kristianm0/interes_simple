# @Kristianmartinezcolina
# ¿Cómo calcular el interés simple con Python?
"""📌 ¿Qué es el interés simple?
Es la ganancia obtenida por invertir dinero durante un tiempo determinado, 
sin que los intereses generados se sumen al capital inicial.
"""
# --- 📖 Ejemplo: Bob Esponja ---
"""
Don Cangrejo invierte $10,000 en un negocio de hamburguesas con una tasa de interés simple del 6%. 
Si deja su inversión durante 45 días, ¿cuánto interés habrá ganado? 
"""
# --- 📝 Fórmula del interés simple ---
# I = P × i × n

""" Datos
📌 Variables:
- I = Interés simple

📌 Datos:
1️⃣ P = Capital inicial o principal
2️⃣ i = Tasa de interés en decimal (Ejemplo: 10% = 0.1, 5% = 0.05) 
    → Se obtiene dividiendo entre 100.
3️⃣ n = Número de períodos de tiempo (años, meses, días)
    → Si es en días, se divide entre 365.
    → Si es en meses, se divide entre 12.
    → Si es en Años, no se hace nada.
"""

# 📌 Función - calcular el interés simple
    #Datos
    tasa_interes = tasa_interes / 100
    principal = principal
    numero_periodo_tiempo = numero_periodo_tiempo / 365

    #Formula
    interes_simple = principal * tasa_interes * numero_periodo_tiempo
    return interes_simple

# 📌 Probamos la función con el caso de Don Cangrejo

# 📌 Mostramos el resultado