@app.route('/admin', methods=['GET', 'POST'])
def admin():
    conn = get_db_connection()
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        imagen = request.form['imagen']
        rubro = request.form['rubro']
        conn.execute('INSERT INTO comercios (nombre, direccion, imagen, rubro) VALUES (?, ?, ?, ?)',
                     (nombre, direccion, imagen, rubro))
        conn.commit()
        return redirect('/admin')
    comercios = conn.execute('SELECT * FROM comercios').fetchall()
    conn.close()
    return render_template('admin.html', comercios=comercios)

