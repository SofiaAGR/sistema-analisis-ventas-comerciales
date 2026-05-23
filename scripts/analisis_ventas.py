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
# calculamos el total de ventas del año
ventas_totales = ventas["sales_amount"].sum()
# calculamos el promedio diario de ventas
promedio_diario = ventas["sales_amount"].mean()
# buscamos el día con mayor facturacion
dia_mayor_venta = ventas.loc[ventas["sales_amount"].idxmax()]
# buscamos el día con menor facturacion
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
