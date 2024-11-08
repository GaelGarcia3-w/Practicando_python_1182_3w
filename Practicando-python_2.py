print()
print("Edgar Gael Garcia Camacho 1182 : Practicando python")
print()
#Se agrega el valor de la variable.
Nota = int(input("Ingresa una nota de una asignación :"))
#Se agrega el valor de la variable para saber si suspendio o si es sobresaliente.
if Nota <= 0 or Nota < 5: 
    print("Suspenso")
elif Nota <= 5 or Nota < 6:
    print("Suficiente")
elif Nota <= 6 or Nota < 7:
    print("Bien")
elif Nota <= 7 or Nota < 8:
    print("Notable")
elif Nota <= 9 or Nota >= 10:
    print("Sobresaliente")
else:
    print("Nota no valida")