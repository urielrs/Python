from flask import Flask, render_template, jsonify
import json
import os

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
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<h2>code</h2><pre>{codigo}</pre>')
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<h2>markdown</h2><p>{texto}</p>')
        
        contenido_html = ''.join(contenido_completo)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
            <style>
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

# Rutas adicionales para otros archivos o contenido
@app.route('/visualizacion-de-datos')
def mostrar_archivo2():
    try:
        archivo_path = '/home/uriel/Documentos/Simulacion/3501_Visualizacion_de_datos.ipynb'
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            return jsonify({'error': f'El archivo {archivo_path} no se encuentra en el sistema'}), 404
        
        with open(archivo_path, 'r', encoding='utf-8') as file:
            contenido_json = json.load(file) 
        
        contenido_completo = []
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<pre>{codigo}</pre>')
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<p>{texto}</p>')
        
        contenido_html = ''.join(contenido_completo)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
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

@app.route('/preparacion-de-datos')
def mostrar_archivo3():
    try:
        archivo_path = '/home/uriel/Documentos/Simulacion/3501_Preparacion_de_datos.ipynb'
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            return jsonify({'error': f'El archivo {archivo_path} no se encuentra en el sistema'}), 404
        
        with open(archivo_path, 'r', encoding='utf-8') as file:
            contenido_json = json.load(file) 
        
        contenido_completo = []
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<pre>{codigo}</pre>')
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<p>{texto}</p>')
        
        contenido_html = ''.join(contenido_completo)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
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

@app.route('/evaluacion-de-resultados')
def mostrar_archivo4():
    try:
        archivo_path = '/home/uriel/Documentos/Simulacion/3501_Evaluacion_de_resultados.ipynb'
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            return jsonify({'error': f'El archivo {archivo_path} no se encuentra en el sistema'}), 404
        
        with open(archivo_path, 'r', encoding='utf-8') as file:
            contenido_json = json.load(file) 
        
        contenido_completo = []
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<pre>{codigo}</pre>')
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<p>{texto}</p>')
        
        contenido_html = ''.join(contenido_completo)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
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

@app.route('/creacion-de-transformadores')
def mostrar_archivo5():
    try:
        archivo_path = '/home/uriel/Documentos/Simulacion/3501_Creacion_de_Transformadores_y_Pipelines_Personalizados.ipynb'
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            return jsonify({'error': f'El archivo {archivo_path} no se encuentra en el sistema'}), 404
        
        with open(archivo_path, 'r', encoding='utf-8') as file:
            contenido_json = json.load(file) 
        
        contenido_completo = []
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<pre>{codigo}</pre>')
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<p>{texto}</p>')
        
        contenido_html = ''.join(contenido_completo)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
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
    

@app.route('/regresion-lineal')
def mostrar_archivo6():
    try:
        archivo_path = '/home/uriel/Documentos/Simulacion/3501_Regresion_Lineal.ipynb'
        
        # Verificar si el archivo existe
        if not os.path.exists(archivo_path):
            return jsonify({'error': f'El archivo {archivo_path} no se encuentra en el sistema'}), 404
        
        with open(archivo_path, 'r', encoding='utf-8') as file:
            contenido_json = json.load(file) 
        
        contenido_completo = []
        
        for celda in contenido_json['cells']:
            if celda['cell_type'] == 'code':
                codigo = ''.join(celda['source'])
                contenido_completo.append(f'<pre>{codigo}</pre>')
            elif celda['cell_type'] == 'markdown':
                texto = ''.join(celda['source'])
                contenido_completo.append(f'<p>{texto}</p>')
        
        contenido_html = ''.join(contenido_completo)
        
        html_contenido = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Archivo Jupyter</title>
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
