from flask import Flask, render_template, jsonify
import json
import os
import base64
from io import BytesIO
import matplotlib.pyplot as plt

app = Flask(__name__)

# Ruta para la página principal que carga index.html
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar el primer archivo (que ya tienes)
@app.route('/regresion-logistica', methods=['GET'])
def mostrar_archivo():
    try:
        archivo_path = '/home/uriel/Documentos/Simulacion/3501_Regresion_logistica.ipynb'
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            return jsonify({'error': f'El archivo {archivo_path} no se encuentra en el sistema'}), 404
        
        with open(archivo_path, 'r', encoding='utf-8') as file:
            contenido_json = json.load(file) 
        
        contenido_completo = []
        imagenes_generadas = []  # Para almacenar imágenes generadas en celdas de código
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<h2>Code</h2><pre>{codigo}</pre>')
                
                # Procesar las salidas de la celda de código, incluyendo gráficas
                for output in celda['outputs']:
                    if 'text/plain' in output['data']:
                        # Verificar si la salida contiene una imagen generada
                        if 'image/png' in output['data']:
                            img_data = output['data']['image/png']
                            img_base64 = base64.b64encode(img_data).decode('utf-8')
                            imagenes_generadas.append(f'<h2>Gráfica</h2><img src="data:image/png;base64,{img_base64}" />')
            
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<h2>Markdown</h2><p>{texto}</p>')
        
        # Unir contenido de Markdown, código y gráficos
        contenido_html = ''.join(contenido_completo + imagenes_generadas)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                }}
                h2 {{
                    color: #2C3E50;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                p {{
                    font-size: 16px;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {contenido_html}
            </div>
        </body>
        </html>
        """
        
        return html_contenido
    
    except FileNotFoundError:
        return jsonify({'error': 'Archivo no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
