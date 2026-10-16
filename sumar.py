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

# 2. Plantilla HTML con menú de selección (Select) renderizada por Django
plantilla_django = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora Interactiva - Django</title>
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .card {
            background: #161b22;
            padding: 2.5rem;
            border-radius: 12px;
            border: 1px solid #30363d;
            box-shadow: 0 8px 24px rgba(0,0,0,0.5);
            text-align: center;
            width: 100%;
            max-width: 400px;
        }
        h1 { color: #58a6ff; margin-bottom: 0.3rem; font-size: 1.8rem; }
        .sub { color: #8b949e; font-size: 0.85rem; margin-bottom: 1.5rem; }
        .input-group { margin-bottom: 1.2rem; text-align: left; }
        label { display: block; margin-bottom: 0.5rem; color: #8b949e; font-size: 0.9rem; }
        input, select {
            width: 100%;
            padding: 0.75rem;
            border-radius: 6px;
            border: 1px solid #30363d;
            background-color: #0d1117;
            color: #f0f6fc;
            font-size: 1rem;
            outline: none;
        }
        input:focus, select:focus { border-color: #58a6ff; }
        button {
            width: 100%;
            padding: 0.75rem;
            background-color: #238636;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            margin-top: 1rem;
            transition: background 0.2s;
        }
        button:hover { background-color: #2ea043; }
        .resultado-box {
            margin-top: 1.5rem;
            padding: 1rem;
            background-color: #1f242c;
            border-radius: 6px;
            border: 1px dashed #30363d;
            display: none;
        }
        .resultado-text { font-size: 1.5rem; color: #3fb950; font-weight: bold; margin: 0; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🧮 Calculadora Web</h1>
        <p class="sub">Renderizado con el motor de plantillas de Django</p>
        
        <div class="input-group">
            <label for="operacion">Selecciona la Operación:</label>
            <select id="operacion">
                <option value="suma">➕ Sumar</option>
                <option value="resta">➖ Restar</option>
            </select>
        </div>

        <div class="input-group">
            <label for="num1">Primer Número:</label>
            <input type="number" id="num1" value="{{ val1_defecto }}" placeholder="Ej. 10">
        </div>
        
        <div class="input-group">
            <label for="num2">Segundo Número:</label>
            <input type="number" id="num2" value="{{ val2_defecto }}" placeholder="Ej. 5">
        </div>
        
        <button onclick="calcular()">Calcular Resultado</button>
        
        <div id="boxResultado" class="resultado-box">
            <p style="margin: 0 0 0.5rem 0; color: #8b949e; font-size: 0.85rem;">Resultado:</p>
            <p id="txtResultado" class="resultado-text">0</p>
        </div>
    </div>

    <script>
        function calcular() {
            const op = document.getElementById('operacion').value;
            const v1 = parseFloat(document.getElementById('num1').value) || 0;
            const v2 = parseFloat(document.getElementById('num2').value) || 0;
            let res = 0;
            let simbolo = '+';

            if (op === 'suma') {
                res = v1 + v2;
                simbolo = '+';
            } else if (op === 'resta') {
                res = v1 - v2;
                simbolo = '-';
            }
            
            document.getElementById('txtResultado').innerText = `${v1} ${simbolo} ${v2} = ${res}`;
            document.getElementById('boxResultado').style.display = 'block';
        }
    </script>
</body>
</html>
"""

# 3. RENDERIZAR con Django pasando valores por defecto
template = Template(plantilla_django)
contexto = Context({"val1_defecto": 15, "val2_defecto": 5})
html_final = template.render(contexto)

# 4. Guardar como archivo index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("Página interactiva index.html renderizada exitosamente con Django.")