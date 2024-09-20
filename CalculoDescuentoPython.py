# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
def main():
    # Primera llamada a la función con solo el monto total (usando el descuento predeterminado del 10%)
    monto_total1 = 100.0
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1
    print(f"Compra de ${monto_total1} con un descuento del 10%: Descuento = ${descuento1:.2f}, Monto final = ${monto_final1:.2f}")

    # Segunda llamada a la función con el monto total y un porcentaje de descuento personalizado
    monto_total2 = 200.0
    porcentaje_descuento2 = 15
    descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    monto_final2 = monto_total2 - descuento2
    print(f"Compra de ${monto_total2} con un descuento del {porcentaje_descuento2}%: Descuento = ${descuento2:.2f}, Monto final = ${monto_final2:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()

