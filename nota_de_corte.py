import os
os.system("clear")
media1 = float(input("Nota media de primero: "))
media2 = float(input("Nota media de segundo: "))
troncales = float(input("Nota media troncales de selectividad: "))
optativa1 = float(input("Nota de una de las optativas: "))
optativa2 = float(input("Nota de la otra optativa: "))
mediaBach = (media1 + media2) / 2

notaCorte = (0.6 * mediaBach) + (0.4 * troncales) + (0.2 * optativa1) + (0.2 * optativa2)

print(f"Tu nota final seria un {notaCorte} sobre 14")
