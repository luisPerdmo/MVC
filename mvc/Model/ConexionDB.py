import mariadb as sql

class ConexionDB():
    def __init__(self):
        self.__host = "localhost" # Cambia si el servidor esta en un host remoto.
        self.__user = "root"
        self.__password = ""
        self.__port = 3308
        self.__database = "mvc"
        self.__conection = None

    def crearConexion(self):
        self.__conection = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            port = self.__port,
            database = self.__database
        )

    def cerrarConexion(self):
        if self.__conection:
            self.__conection.close()
            self.__conection = None

    #poner aqui los getter's y setter's

    def getConection(self):
        return self.__conection