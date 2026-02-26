Para consultar el proyecto se puede visualizar este video de youtube:
https://youtu.be/eGwuHtRaFrM?si=fv1gheal9yeUI2Uo

**Veamos como ya la configuracion de este proyecto de reunir todos los tipos de bases de datos y conexiones:**<br>
gabrielcoga@ToLearn DatabaseProyect % ls -al<br>
total 48<br>
drwxr-xr-x  12 gabrielcoga  staff   384 Jan 19 16:48 .<br>
drwx------@ 13 gabrielcoga  staff   416 Jan 19 16:38 ..<br>
-rw-r--r--@  1 gabrielcoga  staff  8196 Jan 19 16:50 .DS_Store<br>
drwxr-xr-x  12 gabrielcoga  staff   384 Jan 17 23:54 .git<br>
-rw-r--r--@  1 gabrielcoga  staff   392 Jan 16 19:04 .gitignore<br>
drwxr-xr-x@  7 gabrielcoga  staff   224 Jan 19 16:48 .venv<br>
drwxr-xr-x   7 gabrielcoga  staff   224 Jan 16 19:00 DatabaseFile<br>
drwxr-xr-x   7 gabrielcoga  staff   224 Jan 16 19:00 DatabaseJSON<br>
drwxr-xr-x   6 gabrielcoga  staff   192 Jan 16 19:00 DatabaseList<br>
drwxr-xr-x   3 gabrielcoga  staff    96 Jan 19 16:37 DatabaseMysql<br>
drwxr-xr-x   9 gabrielcoga  staff   288 Jan 16 19:01 DatabaseSqlite<br>
-rw-r--r--@  1 gabrielcoga  staff  6605 Jan 17 23:54 README.md<br>

**Activacion del Entorno Virtual ya creado:**<br>
gabrielcoga@ToLearn DatabaseProyect % source .venv/bin/activate<br>

(.venv) gabrielcoga@ToLearn DatabaseProyect % which python<br>
/Users/gabrielcoga/Documents/DatabaseProyect/.venv/bin/python<br>

**Instalamos dentro del entorno virtual el conector de la base de datos para utilizarla dentro de los modulos python:**<br>
(.venv) gabrielcoga@ToLearn DatabaseProyect % pip3 install mysql-connector-python<br>
Collecting mysql-connector-python<br>
  Downloading mysql_connector_python-9.4.0-cp39-cp39-macosx_14_0_x86_64.whl.metadata (7.3 kB)<br>
Downloading mysql_connector_python-9.4.0-cp39-cp39-macosx_14_0_x86_64.whl (18.4 MB)<br>
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 18.4/18.4 MB 8.7 MB/s  0:00:02<br>
Installing collected packages: mysql-connector-python<br>
Successfully installed mysql-connector-python-9.4.0<br>

(.venv) gabrielcoga@ToLearn DatabaseProyect % <br>

**Una vez instalado el Servidor de Bases de Datos en tu PC, procedemos a lanzarlo y a entrar para crear la base de datos y las tablas:**<br>

gabrielcoga@ToLearn ~ % mysql -u root            

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 9.6.0 Homebrew

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 

**Vamos a crear la base de datos y las tablas que necesitamos para este ejercicio:**<br>

mysql> CREATE DATABASE projects;<br>
Query OK, 1 row affected (0,003 sec)<br>

mysql> use projects;
Database changed
mysql> 

mysql> CREATE TABLE projects(project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id));
Query OK, 0 rows affected, 1 warning (0,027 sec)

mysql> 

mysql> show tables;
+--------------------+
| Tables_in_projects |
+--------------------+
| projects           |
+--------------------+
1 row in set (0,005 sec)

mysql> 


