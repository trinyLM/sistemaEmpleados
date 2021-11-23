# se crea una base de datos
CREATE DATABASE sistema_empleado;
use DATABASE sistema_empleado;

# creamos la tabla don se almacenaran los datos de los empleados 
create TABLE empleados(id integer(100) AUTO_INCREMENT not null PRIMARY key ,nombre varchar(100)not null,apellido varchar(100) not null, genero varchar(20)not null, fecha_nacimiento date NOT null, fecha_ingreso date not null, salario_basico float not null);

#insertamos los primeros valores para visulaizar nustra base de datos
insert into empleados (nombre,apellido, genero, fecha_nacimiento,fecha_ingreso,salario_basico)values('Trinidad','Luna','Masculino','2000-06-18','2018-08-25',4800.00);

#actualizar los datros de la tabla