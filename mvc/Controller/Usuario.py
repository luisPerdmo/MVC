from Model.ConexionDB import ConexionDB
from tkinter import messagebox

from View.ConsultarUsuarios import ConsultarUsuario

class Usuario():
    def __init__(self):
        self.__cedula = None
        self.__nombre = None
        self.__rol = None

    #poner aqui getter's y setter's

    def iniciarSesion(self, nombreUsuario, password, loggin):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        for usuario in listaUsuario:
            if(usuario[2] == nombreUsuario and usuario[1] == password):
                self.cedula = usuario[1]
                self.nombre = usuario[2]
                self.rol = usuario[3]
                if(usuario[3] == "Admin"):    
                    messagebox.showinfo("informacion", "Acceso Correcto Administrador")
                    miMenu = ConsultarUsuario(loggin, self)
                else:
                    messagebox.showinfo("informacion", "Acceso Correcto USuario")  
                miConexion.cerrarConexion()
                return
        messagebox.showwarning("Advertencia", "El nombre de usuario y/o contraseña no existe, verifique e intente nuevamente!")

    def consultarTabla(self):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("Select * from usuario")
        listaUsuario = cursor.fetchall()
        return listaUsuario
    
    def crearUsuario(self, nombreUsuario, cedulaUsuario, rolUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuario (cedula, nombre, rol) VALUES (?, ?, ?)", (cedulaUsuario, nombreUsuario, rolUsuario))
        miConexion.cerrarConexion

    def eliminarUsuario(self, cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("DELETE from usuario WHERE cedula = " + cedulaUsuario)
        miConexion.cerrarConexion

    def modificarUsuario(self, nombreUsuario, cedulaUsuario, rolUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuario SET nombre=?, rol=? WHERE cedula=?", (nombreUsuario, rolUsuario, cedulaUsuario))
        miConexion.cerrarConexion
    
    def buscarUsuario(self, cedulaUsuario):
        miConexion = ConexionDB()
        miConexion.crearConexion()
        conexion = miConexion.getConection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * from usuario WHERE cedula=" + cedulaUsuario)
        listaUsuario = cursor.fetchall()
        miConexion.cerrarConexion
        if (len(listaUsuario)) > 0:
            usuario = listaUsuario[0]
            return usuario
        else:
            return None