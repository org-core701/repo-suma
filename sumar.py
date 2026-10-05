import sys
import os

# Recibir los dos números desde la consola/Action o usar 10 y 20 por defecto
num1 = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] != '' else 10
num2 = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != '' else 20

resultado = num1 + num2

print("==================================")
print(f"Ejecutando script: sumar.py")
print(f"Suma: {num1} + {num2} = {resultado}")
print("==================================")

# Publicar el resultado directamente en el resumen visual de GitHub
summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
if summary_file:
    with open(summary_file, 'a') as f:
        f.write("## 🧮 Resultado del Script Python (`sumar.py`)\n")
        f.write(f"- **Primer Número:** {num1}\n")
        f.write(f"- **Segundo Número:** {num2}\n")
        f.write(f"- **Resultado Total:** `{resultado}`\n")