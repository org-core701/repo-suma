import django
from django.conf import settings
from django.template import Template, Context

# 1. Configurar el motor de plantillas de Django
if not settings.configured:
    settings.configure(
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
        }]
    )
django.setup()

# 2. Plantilla con sintaxis oficial de Django (variables entre {{ }})
plantilla_django = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Calculadora de Resta - Django</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: Arial, sans-serif; background: #0d1117; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #161b22; padding: 2rem; border-radius: 12px; border: 1px solid #30363d; text-align: center; width: 350px; }
        h1 { color: #f85149; }
        input { width: 100%; padding: 0.7rem; margin: 0.5rem 0; background: #0d1117; border: 1px solid #30363d; color: white; border-radius: 6px; }
        button { width: 100%; padding: 0.7rem; background: #da3633; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; margin-top: 1rem; }
        .res { margin-top: 1rem; color: #f85149; font-size: 1.4rem; font-weight: bold; }
        a { color: #58a6ff; text-decoration: none; display: inline-block; margin-top: 1rem; }
    </style>
</head>
<body>
    <div class="card">
        <h1>➖ Restar Dos Números</h1>
        <p style="color: #8b949e; font-size: 0.8rem;">Renderizado con el motor de Django</p>
        
        <input type="number" id="n1" value="{{ num1_defecto }}" placeholder="Número 1">
        <input type="number" id="n2" value="{{ num2_defecto }}" placeholder="Número 2">
        <button onclick="calcularResta()">Calcular Resta</button>
        
        <div id="resultado" class="res"></div>
        <br>
        <a href="index.html">⬅️ Ir a la Suma</a>
    </div>

    <script>
        function calcularResta() {
            const a = parseFloat(document.getElementById('n1').value) || 0;
            const b = parseFloat(document.getElementById('n2').value) || 0;
            document.getElementById('resultado').innerText = `${a} - ${b} = ${a - b}`;
        }
    </script>
</body>
</html>
"""

# 3. RENDERIZAR con Django
template = Template(plantilla_django)
contexto = Context({"num1_defecto": 50, "num2_defecto": 20})
html_renderizado = template.render(contexto)

# 4. Guardar la página de resta
with open("resta.html", "w", encoding="utf-8") as f:
    f.write(html_renderizado)

print("Página resta.html RENDERIZADA exitosamente con Django.")