# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Escritura de Archivo de Texto
# Abrimos el archivo en modo escritura (write)
with open(file_name, 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Nota 1: Recordar comprar víveres.\n")
    file.write("Nota 2: Reunión con el equipo a las 3 PM.\n")
    file.write("Nota 3: Terminar el informe del proyecto.\n")

# Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura (read)
with open(file_name, 'r') as file:
    # Leemos el contenido línea por línea
    for line in file:
        # Mostramos en la consola cada línea leída
        print(line.strip())  # strip() elimina los espacios en blanco y saltos de línea

# Cierre de Archivos
# No es necesario cerrar el archivo explícitamente al usar 'with', se cierra automáticamente


