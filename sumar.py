import os

# Generar un archivo index.html totalmente interactivo
contenido_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de Suma - Organización</title>
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
        h1 { color: #58a6ff; margin-bottom: 1.5rem; font-size: 1.8rem; }
        .input-group { margin-bottom: 1.2rem; text-align: left; }
        label { display: block; margin-bottom: 0.5rem; color: #8b949e; font-size: 0.9rem; }
        input {
            width: 100%;
            padding: 0.75rem;
            border-radius: 6px;
            border: 1px solid #30363d;
            background-color: #0d1117;
            color: #f0f6fc;
            font-size: 1rem;
            outline: none;
        }
        input:focus { border-color: #58a6ff; }
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
        <h1>🧮 Sumar Dos Números</h1>
        
        <div class="input-group">
            <label for="num1">Primer Número:</label>
            <input type="number" id="num1" placeholder="Ej. 10" value="10">
        </div>
        
        <div class="input-group">
            <label for="num2">Segundo Número:</label>
            <input type="number" id="num2" placeholder="Ej. 20" value="20">
        </div>
        
        <button onclick="calcularSuma()">Calcular Suma</button>
        
        <div id="boxResultado" class="resultado-box">
            <p style="margin: 0 0 0.5rem 0; color: #8b949e; font-size: 0.85rem;">Resultado:</p>
            <p id="txtResultado" class="resultado-text">0</p>
        </div>
    </div>

    <script>
        function calcularSuma() {
            const val1 = parseFloat(document.getElementById('num1').value) || 0;
            const val2 = parseFloat(document.getElementById('num2').value) || 0;
            const suma = val1 + val2;
            
            document.getElementById('txtResultado').innerText = `${val1} + ${val2} = ${suma}`;
            document.getElementById('boxResultado').style.display = 'block';
        }
    </script>
</body>
</html>
"""

# Guardar la página web
with open("index.html", "w", encoding="utf-8") as f:
    f.write(contenido_html)

print("Página interactiva index.html generada exitosamente.")
"""