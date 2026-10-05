import sys
import os

# Recibir variables de la consola
num1 = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1] != '' else 10
num2 = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != '' else 20

resultado = num1 + num2

print("==================================")
print(f"Suma realizada: {num1} + {num2} = {resultado}")
print("==================================")

# 1. Emitir una anotación destacada en la interfaz de GitHub
print(f"::notice title=Suma Exitosa::El resultado es {resultado}. Puedes visitar la organización en https://github.com/org-core701")

# 2. Escribir el resumen visual con enlace interactivo
summary_file = os.environ.get('GITHUB_STEP_SUMMARY')
if summary_file:
    with open(summary_file, 'a') as f:
        f.write("## 🧮 Resultado del Script Python (`sumar.py`)\n\n")
        f.write(f"* **Primer Número:** `{num1}`\n")
        f.write(f"* **Segundo Número:** `{num2}`\n")
        f.write(f"* **Resultado Total:** `{resultado}`\n\n")
        f.write("---\n")
        # Enlace directo
        f.write("🔗 **Enlace rápido:** [Ver Repositorio de la Organización](https://github.com/org-core701/repo-suma)\n")