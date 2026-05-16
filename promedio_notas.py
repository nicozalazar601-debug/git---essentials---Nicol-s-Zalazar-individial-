#Archivo modificado 
# Programa individual - Nicolas Zalazar

print("================================")
print("   Calculadora de Promedio UTN  ")
print("================================")

nombre = input("Ingrese su nombre: ")
cantidad = int(input("¿Cuantas notas quiere ingresar? "))

notas = []

for i in range(cantidad):
    nota = float(input(f"Ingrese nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("\n================================")
print(f"  Alumno: {nombre}")
print(f"  Promedio: {promedio:.2f}")

if promedio >= 6:
    print("  Estado: APROBADO ✅")
else:
    print("  Estado: DESAPROBADO ❌")

print("================================")
