import feistel, hashlib, pathlib, base64
from io import open  # para abrir archivos

# Key y modo
modo = "ecb"
key = "qwerty"

# lectura de archivo mensajedeentrada
ruta = str(pathlib.Path().absolute()) + "/mensajedeentrada.txt"
archivo = open(ruta, "r")
mensaje = archivo.readlines()
archivo.close()
mensaje = mensaje[0]
print(f"texto sin formato: {mensaje}")

# hash
result = hashlib.md5(mensaje.encode())
hash1 = result.hexdigest()

# cifrado
mensaje_cifrado = feistel.encryptMessage(key, mensaje, modo)

mensaje_cifrado_encode = bytearray(mensaje_cifrado.encode())
finalResult = base64.b64encode(mensaje_cifrado_encode)

# guardando cifrado en mensajeseguro
ruta = str(pathlib.Path().absolute()) + "/mensajeseguro.txt"
archivo1 = open(ruta, "w", encoding="utf-8")
archivo1.write(str(finalResult, "utf-8"))
archivo1.close()

# lectura de archivo mensajeseguro
ruta = str(pathlib.Path().absolute()) + "/mensajeseguro.txt"
archivo2 = open(ruta, "r")
mensaje = archivo2.readlines()
archivo2.close()
mensaje = mensaje[0]

# descifrado
# se pasa a bytes para pasarlo como parametro al base64, ya que se habia guardado en el archivo como string
mensajeByte = bytes(mensaje, 'utf-8')
decodedB64mensajeDecrypt = base64.b64decode(mensajeByte)
barrayencode = bytearray(decodedB64mensajeDecrypt)
mensaje1 = str(barrayencode, "utf-8")
mensaje_descifrado = feistel.decryptCipher(key, mensaje1, modo)
print(f"mensaje descifrado: {mensaje_descifrado}")

# hash
result2 = hashlib.md5(mensaje_descifrado.encode())
hash2 = result2.hexdigest()

# comparacion
if hash1 == hash2:
    print("El mensaje no ha sido modificado")
else:
    print("el mensaje ha sido modificado")

print(f"""
hash mensaje original: {hash1}
hash mensaje descifrado: {hash2}   
""")