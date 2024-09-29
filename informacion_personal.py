# Crear un diccionario llamado 'informacion_personal' con datos ficticios
informacion_personal = {
    "nombre": "Ana Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniera de software"
}

# Acceder al valor asociado con la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

# Modificar el valor de "ciudad" a una nueva ciudad
informacion_personal["ciudad"] = "Guayaquil"
print(f"Ciudad modificada: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para "telefono"
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"
    print(f"Clave 'telefono' agregada: {informacion_personal['telefono']}")

# Imprimir el diccionario actualizado
print("\nInformación personal actualizada:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

