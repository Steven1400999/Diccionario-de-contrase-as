import itertools

def generar_contraseñas(longitud):
    caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789'
    contraseñas = []
    for longitud_contraseña in range(longitud, longitud + 1):
        for combinacion in itertools.product(caracteres, repeat=longitud_contraseña):
            contraseña = ''.join(combinacion)
            contraseñas.append(contraseña)
    return contraseñas

def guardar_contraseñas(contraseñas, nombre_archivo):
    with open(nombre_archivo, 'w') as f:
        for contraseña in contraseñas:
            f.write(contraseña + '\n')

def main():
    longitud = 4  # Longitud de las contraseñas
    contraseñas = generar_contraseñas(longitud)
    nombre_archivo = 'contraseñas.txt'
    guardar_contraseñas(contraseñas, nombre_archivo)
    print(f"Se han guardado las contraseñas en {nombre_archivo}")

if __name__ == "__main__":
    main()
