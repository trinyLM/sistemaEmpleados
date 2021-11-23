from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import date

app=Flask(__name__)
# SE CONECTA A LA BA SE DE DATOS
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_empleado'
mysql.init_app(app)



#RENDERIZAMOS NUESTRA PAGINA WEB 
@app.route("/")
def index():
    sql='SELECT * FROM `empleados`'#la secuencia sql a ejecutarse
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()

    conn.commit()

    return render_template('index.html', empleados=empleados)


@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/almacenar', methods=['POST'])
def almacenar():
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _genero=request.form['txtGenero']
    _fecha_nacimiento=request.form['dateNacimiento']
    _fecha_ingreso=request.form['dateIngreso']
    _salario=request.form['salario']
    sql="insert into empleados (nombre,apellido, genero, fecha_nacimiento,fecha_ingreso,salario_basico)values('{0}','{1}','{2}','{3}','{4}','{5}');".format(_nombre,_apellido,_genero,_fecha_nacimiento,_fecha_ingreso,_salario)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return redirect('/')

#eliminaños los ddatos medinate la id de cada empleado
@app.route('/destroy/<int:id>')
def eliminar(id):
    sql="delete from empleados where id={}".format(id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    
    return redirect('/') 


@app.route('/editar/<int:id>')
def editar(id):
    sql='SELECT * FROM `empleados`where id={}'.format(id)#la secuencia sql a ejecutarse
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    conn.commit()
    return render_template('/editar.html', empleados=empleados)

@app.route('/almacen_editar', methods=['POST'])
def almacen_editar():
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _genero=request.form['txtGenero']
    _fecha_nacimiento=request.form['dateNacimiento']
    _fecha_ingreso=request.form['dateIngreso']
    _salario=request.form['salario']
    id=request.form['txt_id']
    sql="update empleados set nombre='{0}',apellido='{1}',genero='{2}',fecha_nacimiento='{3}', fecha_ingreso='{4}', salario_basico='{5}' where id='{6}';".format(_nombre,_apellido,_genero,_fecha_nacimiento,_fecha_ingreso,_salario,id)
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return redirect('/')



@app.route('/masInfo/<int:id>')
def informar(id):
    sql='SELECT * FROM `empleados`where id={}'.format(id)#la secuencia sql a ejecutarse
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    conn.commit()
    today = date.today()     
    return render_template('info.html', empleados=empleados,today=today)
    


if __name__== '__main__':
    app.run(debug=True) 