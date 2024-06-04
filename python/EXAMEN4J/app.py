import os
from flask import Flask, render_template, request, redirect, url_for, flash
import database as db

class InvalidNotaError(Exception):
    pass

# Configura la ruta del directorio de plantillas
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'andre'

# Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM martinez")
    myresult = cursor.fetchall()
    # Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

# Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    id = request.form['id']
    nombre = request.form['nombre']
    asignatura = request.form['asignatura']
    nota = request.form['nota']

    try:
        # Validar que "nota" sea un entero
        if not nota.isdigit():
            raise InvalidNotaError("La nota debe ser un número entero.")
        
        nota = int(nota)  # Convertir "nota" a entero

        if id and nombre and asignatura and nota:
            cursor = db.database.cursor()
            sql = "INSERT INTO martinez (id, nombre, asignatura, nota) VALUES (%s, %s, %s, %s)"
            data = (id, nombre, asignatura, nota)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('home'))
    except InvalidNotaError as e:
        flash(str(e))
        return redirect(url_for('home'))
    except Exception as e:
        flash("Ocurrió un error al agregar el usuario.")
        return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM martinez WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    asignatura = request.form['asignatura']
    nota = request.form['nota']

    try:
        # Validar que "nota" sea un entero
        if not nota.isdigit():
            raise InvalidNotaError("La nota debe ser un número entero.")
        
        nota = int(nota)  # Convertir "nota" a entero

        if nombre and asignatura and nota:
            cursor = db.database.cursor()
            sql = "UPDATE martinez SET nombre = %s, asignatura = %s, nota = %s WHERE id = %s"
            data = (nombre, asignatura, nota, id)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('home'))
    except InvalidNotaError as e:
        flash(str(e))
        return redirect(url_for('home'))
    except Exception as e:
        flash("Ocurrió un error al editar el usuario.")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5500)