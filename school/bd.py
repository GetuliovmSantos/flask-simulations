import mysql.connector
import mysql.connector.errors

class BD:
    _connection = None

    def connect(self):
        try:
            if self._connection is not None:
                return self._connection
            self._connection = mysql.connector.connect(
                host="localhost",
                port="3306",
                user="root",
                password="",
                database="school-flask"
            )
            return self._connection
        except mysql.connector.errors.ProgrammingError as e:
            print('Error:', e)
            return {'error': e}
        
    def close(self):
        self._connection.close()
        self._connection = None

    def login(self, loginUsuario, senhaUsuario):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM usuarios WHERE loginUsuario='{loginUsuario}' AND senhaUsuario='{senhaUsuario}'")
        result = cursor.fetchone()
        cursor.close()
        self.close()
        if result is not None:
            return {
                'loginUsuario': result[1],
                'senhaUsuario': result[2]
            }
        else:
            return {"error": "Usuário não encontrado"}
        
    def recuperarsenha(self, loginUsuario, senhaUsuario, cSenhaUsuario):
        self.connect()
        cursor = self._connection.cursor()
        
        cursor.execute(f"SELECT * FROM usuarios WHERE loginUsuario='{loginUsuario}'")
        result = cursor.fetchone()
        if result is None:
            cursor.close()
            self.close()
            return {"error": "Usuário não encontrado"}
        elif senhaUsuario != cSenhaUsuario:
            cursor.close()
            self.close()
            return {"error": "As senhas não coincidem"}
        else:
            cursor.execute(f"UPDATE usuarios SET senhaUsuario='{senhaUsuario}' WHERE loginUsuario='{loginUsuario}'")
            self._connection.commit()
            cursor.close()
            self.close()
            return {"success": "Senha alterada com sucesso"}