import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", user="root", passwd="Styfler01", database="bd1") #,auth_plugin='mysql_native_password'
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cone.commit()
        cursor.execute(sql, datos)
        datas =cursor.fetchall()
        cone.close()
        return datas

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select codigo, descripcion, precio from bd1.articulos"
        cursor.execute(sql)
        datas = cursor.fetchall()
        cone.close()
        return datas
    

