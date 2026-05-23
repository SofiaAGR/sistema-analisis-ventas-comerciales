# importamos pandas para trabajar con tablas y poder analizar datos
import pandas as pd
# importamos matplotlib para generar los graficos
import matplotlib.pyplot as plt

# CARGA DEL DATASET
# leemos el archivo CSV ubicado en la carpeta datos
ventas = pd.read_csv("datos/sales_sample_2024.csv")
# eliminamos espacios innecesarios en los nombres de columnas (para seguir buenas practicas)
ventas.columns = ventas.columns.str.strip()
# convertimos la columna de fechas para poder trabajar por mes.
ventas["sales_date"] = pd.to_datetime(ventas["sales_date"])

# CALCULO DE METRICAS

# Utilizamos sum() para obtener la suma total de la columna sales_amount.
# Esto nos permite conocer la facturación total registrada durante el año
# y tener una referencia general del desempeño comercial.
ventas_totales = ventas["sales_amount"].sum()

# Utilizamos mean() para calcular el promedio de ventas diarias.
# Esta métrica sirve para conocer el comportamiento promedio de las ventas
# y poder comparar distintos períodos contra un valor de referencia.
promedio_diario = ventas["sales_amount"].mean()

# Utilizamos idxmax() para encontrar la posición donde se encuentra
# la venta más alta del dataset. Luego usamos loc[] para acceder
# a toda la información de ese registro, incluyendo fecha y monto.
# Esto permite identificar el día de mayor facturación del año.
dia_mayor_venta = ventas.loc[ventas["sales_amount"].idxmax()]

# Del mismo modo, utilizamos idxmin() para encontrar la posición de la venta más baja
# registrada en el dataset. Después utilizamos loc[] para obtener
# toda la información correspondiente a ese día.
# Esto ayuda a identificar períodos de menor actividad comercial.
dia_menor_venta = ventas.loc[ventas["sales_amount"].idxmin()]

# ANALISIS MENSUAL
# creamos una columna con el mes correspondiente de cada venta
ventas["mes"] = ventas["sales_date"].dt.strftime("%Y-%m")
# agrupamos las ventas por mes y sumamos los montos
ventas_mensuales = ventas.groupby("mes")["sales_amount"].sum()

# RESULTADOS
# generamos un archivo de texto con el resumen del analisis
with open("resultados/resumen_ventas.txt", "w", encoding="utf-8") as archivo:

    archivo.write("Resumen de Ventas Año 2024\n")
    archivo.write("==========================\n\n")

    archivo.write(f"Ventas totales del año: ${ventas_totales:.2f}\n")
    archivo.write(f"Promedio de ventas diarias: ${promedio_diario:.2f}\n")

    archivo.write(
        f"Día de mayor facturación: "
        f"{dia_mayor_venta['sales_date'].date()} - "
        f"${dia_mayor_venta['sales_amount']:.2f}\n"
    )

    archivo.write(
        f"Día de menor facturación: "
        f"{dia_menor_venta['sales_date'].date()} - "
        f"${dia_menor_venta['sales_amount']:.2f}\n\n"
    )

    archivo.write("Ventas mensuales:\n")
    archivo.write(ventas_mensuales.to_string())

# GRAFICO
# configuramos el tamaño del grafico
plt.figure(figsize=(10, 5))
# generamos un grafico de barras con las ventas mensuales
ventas_mensuales.plot(kind="bar")
# agregamos titulo y nombres a los ejes
plt.title("Ventas mensuales - Año 2024")
plt.xlabel("Mes")
plt.ylabel("Monto de ventas")
# ajustamos automaticamente los margenes
plt.tight_layout()
# guardamos el grafico dentro de la carpeta resultados
plt.savefig("resultados/ventas_mensuales_2024.png")
# cerramos el grafico
plt.close()

# MENSAJES FINALES
print("Análisis finalizado correctamente.")
print()
print(f"Ventas totales del año: ${ventas_totales:.2f}")
print(f"Promedio de ventas diarias: ${promedio_diario:.2f}")
print(f"Día de mayor facturación: {dia_mayor_venta['sales_date'].date()}")
print(f"Día de menor facturación: {dia_menor_venta['sales_date'].date()}")
print()
print("Resultados guardados en la carpeta /resultados.")
