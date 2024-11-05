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
                database="school-flask",
            )
            return self._connection
        except mysql.connector.errors.ProgrammingError as e:
            print("Error:", e)
            return {"error": e}

    def close(self):
        self._connection.close()
        self._connection = None

    # Métodos relacionados ao usuário
    def login(self, loginUsuario, senhaUsuario):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(
            f"SELECT * FROM usuarios WHERE loginUsuario='{loginUsuario}' AND senhaUsuario='{senhaUsuario}'"
        )
        result = cursor.fetchone()
        cursor.close()
        self.close()
        if result is not None:
            return {
                "loginUsuario": result[0],
                "nomeUsuario": result[1],
                "senhaUsuario": result[2],
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
            cursor.execute(
                f"UPDATE usuarios SET senhaUsuario='{senhaUsuario}' WHERE loginUsuario='{loginUsuario}'"
            )
            self._connection.commit()
            cursor.close()
            self.close()
            return {"success": "Senha alterada com sucesso"}

    # Métodos relacionados às turmas
    def buscarTurmas(self, loginUsuario):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM turmas WHERE loginUsuario='{loginUsuario}'")
        result = cursor.fetchall()
        cursor.close()
        self.close()

        turmas = []

        if len(result) > 0:
            for turma in result:
                turmas.append(
                    {
                        "codTurma": turma[0],
                        "nomeTurma": turma[1],
                        "periodoTurma": turma[2],
                    }
                )

        return turmas

    def buscarTurma(self, codTurma):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM turmas WHERE codTurma={codTurma}")
        result = cursor.fetchone()
        cursor.close()
        self.close()

        if result is not None:
            return {
                "codTurma": result[0],
                "nomeTurma": result[1],
                "periodoTurma": result[2],
            }
        else:
            return {"error": "Turma não encontrada"}

    def salvarTurma(self, loginUsuario, nomeTurma, periodoTurma):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(
            f"INSERT INTO turmas (loginUsuario, nomeTurma, periodoTurma) VALUES ('{loginUsuario}', '{nomeTurma}', '{periodoTurma}')"
        )
        self._connection.commit()
        cursor.close()
        self.close()
        return {"success": "Turma adicionada com sucesso"}

    def excluirTurma(self, codTurma):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM turmas WHERE codTurma={codTurma}")
        self._connection.commit()
        cursor.close()
        self.close()
        return {"success": "Turma excluída com sucesso"}

    def atualizarTurma(self, codTurma, nomeTurma, periodoTurma):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(
            f"""
            UPDATE turmas
            SET nomeTurma='{nomeTurma}', periodoTurma='{periodoTurma}'
            WHERE codTurma={codTurma}
        """
        )
        self._connection.commit()
        cursor.close()
        self.close()
        return {"success": "Turma atualizada com sucesso"}

    # Métodos relacionados às atividades
    def buscarAtividades(self, codTurma):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM atividades WHERE codTurma={codTurma}")
        result = cursor.fetchall()
        cursor.close()
        self.close()

        atividades = []

        if len(result) > 0:
            for atividade in result:
                atividades.append(
                    {
                        "idAtividade": atividade[0],
                        "nomeAtividade": atividade[1],
                        "descricaoAtividade": atividade[2],
                        "dataAtividade": atividade[3],
                        "pesoAtividade": atividade[4],
                    }
                )

        return atividades

    def buscarAtividade(self, idAtividade):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT * FROM atividades WHERE idAtividade={idAtividade}")
        result = cursor.fetchone()
        cursor.close()
        self.close()

        if result is not None:
            return {
                "idAtividade": result[0],
                "nomeAtividade": result[1],
                "descricaoAtividade": result[2],
                "dataAtividade": result[3],
                "pesoAtividade": result[4],
            }
        else:
            return {"error": "Atividade não encontrada"}

    def salvarAtividade(
        self, nomeAtividade, descricaoAtividade, dataEntrega, pesoAtividade, codTurma
    ):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(
            f"""
            INSERT INTO atividades (nomeAtividade, descricaoAtividade, dataAtividade, pesoAtividade, codTurma)
            VALUES ('{nomeAtividade}', '{descricaoAtividade}', '{dataEntrega}', '{pesoAtividade}', {codTurma})
        """
        )
        self._connection.commit()
        cursor.close()
        self.close()
        return {"success": "Atividade adicionada com sucesso"}

    def excluirAtividade(self, idAtividade):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM atividades WHERE idAtividade={idAtividade}")
        self._connection.commit()
        cursor.close()
        self.close()
        return {"success": "Atividade excluída com sucesso"}

    def atualizarAtividade(self, codAtividade, nomeAtividade, descricaoAtividade, dataAtividade, pesoAtividade):
        self.connect()
        cursor = self._connection.cursor()
        cursor.execute(
            f"""
            UPDATE atividades
            SET nomeAtividade='{nomeAtividade}', descricaoAtividade='{descricaoAtividade}', dataAtividade='{dataAtividade}', pesoAtividade='{pesoAtividade}'
            WHERE idAtividade={codAtividade}
        """
        )
        self._connection.commit()
        cursor.close()
        self.close()
        return {"success": "Atividade atualizada com sucesso"}