import sys

def leer_entrada():
    if len(sys.argv) >= 3:
        return int(sys.argv[1]), int(sys.argv[2])
    
    datos = sys.stdin.read().strip().split()
    if len(datos) >= 2:
        return int(datos[0]), int(datos[1])

    sys.exit(1)

a, b = leer_entrada()

print(a + b)