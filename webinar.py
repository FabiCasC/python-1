import random
import string

# Generador de contraseñas
longitud = int(input('Ingrese la longitud de la contraseña: '))
caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
print(f'Contraseña generada: {contraseña}')
