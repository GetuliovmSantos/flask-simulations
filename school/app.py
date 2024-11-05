from flask import Flask, render_template, request, redirect
from bd import BD

app = Flask(__name__)
bd = BD()
usuario = None

# Rotas relacionadas ao usuário
@app.route("/")
def index():
    # Conecta ao banco de dados
    connection = bd.connect()

    # Verifica se houve erro na conexão
    if "error" in str(connection):
        return render_template("index.html", error=connection["error"])

    bd.close()

    return render_template("index.html", error=None)


@app.route("/logar", methods=["POST"])
def logar():
    global usuario

    # Obtém login e senha do formulário
    login = request.form["login"]
    senha = request.form["senha"]
    
    # Tenta logar o usuário
    usuario = bd.login(login, senha)
    
    # Verifica se houve erro no login
    if "error" in usuario:
        return render_template("index.html", error=usuario["error"])
    else:
        return redirect("/turmas")


@app.route("/esqueciSenha")
def esqueciSenha():
    return render_template("esqueciSenha.html", error=None)


@app.route("/recuperarSenha", methods=["POST"])
def recuperarSenha():
    # Obtém login, nova senha e confirmação de senha do formulário
    login = request.form["login"]
    senha = request.form["senha"]
    cSenha = request.form["cSenha"]

    # Tenta recuperar a senha
    result = bd.recuperarsenha(login, senha, cSenha)

    # Verifica se houve erro na recuperação de senha
    if "error" in result:
        return render_template("esqueciSenha.html", error=result["error"])
    else:
        return redirect("/")

# Rotas relacionadas às turmas
@app.route("/turmas")
def turmas():
    # Busca as turmas do usuário logado
    turmas = bd.buscarTurmas(usuario["loginUsuario"])

    return render_template("turmas.html", usuario=usuario, turmas=turmas)


@app.route("/adicionarTurma")
def adicionarTurma():
    return render_template("adicionarTurma.html", usuario=usuario)


@app.route("/salvarTurma", methods=["POST"])
def salvarTurma():
    # Obtém nome e período da turma do formulário
    nomeTurma = request.form["nomeTurma"]
    periodoTurma = request.form["periodoTurma"]
    
    # Salva a nova turma no banco de dados
    bd.salvarTurma(usuario["loginUsuario"], nomeTurma, periodoTurma)

    return redirect("/turmas")


@app.route("/excluirTurma/<int:codTurma>")
def excluirTurma(codTurma):
    # Exclui a turma especificada
    bd.excluirTurma(codTurma)
    return redirect("/turmas")


@app.route("/editarTurma/<int:codTurma>")
def editarTurma(codTurma):
    # Busca os dados da turma especificada
    turma = bd.buscarTurma(codTurma)
    return render_template(
        "editarTurma.html", usuario=usuario, turma=turma, codTurma=codTurma
    )


@app.route("/atualizarTurma/<int:codTurma>", methods=["POST"])
def atualizarTurma(codTurma):
    # Obtém novos dados da turma do formulário
    nomeTurma = request.form["nomeTurma"]
    periodoTurma = request.form["periodoTurma"]
    
    # Atualiza a turma no banco de dados
    bd.atualizarTurma(codTurma, nomeTurma, periodoTurma)
    return redirect("/turmas")

# Rotas relacionadas às atividades
@app.route("/adicionarAtividade/<int:codTurma>")
def adicionarAtividade(codTurma):
    return render_template(
        "adicionarAtividade.html", usuario=usuario, codTurma=codTurma
    )


@app.route("/salvarAtividade/<int:codTurma>", methods=["POST"])
def salvarAtividade(codTurma):
    # Obtém dados da atividade do formulário
    nomeAtividade = request.form["nomeAtividade"]
    descricaoAtividade = request.form["descricaoAtividade"]
    pesoAtividade = request.form["pesoAtividade"]
    dataAtividade = request.form["dataAtividade"]
    
    # Salva a nova atividade no banco de dados
    bd.salvarAtividade(
        nomeAtividade, descricaoAtividade, dataAtividade, pesoAtividade, codTurma
    )
    return redirect("/turmas")


@app.route("/verAtividades/<int:codTurma>")
def verAtividades(codTurma):
    # Busca as atividades da turma especificada
    atividades = bd.buscarAtividades(codTurma)
    return render_template(
        "verAtividades.html", usuario=usuario, atividades=atividades, codTurma=codTurma
    )


@app.route("/excluirAtividade/<int:codAtividade>")
def excluirAtividade(codAtividade):
    # Exclui a atividade especificada
    bd.excluirAtividade(codAtividade)
    return redirect("/turmas")


@app.route("/editarAtividade/<int:codAtividade>")
def editarAtividade(codAtividade):
    # Busca os dados da atividade especificada
    atividade = bd.buscarAtividade(codAtividade)
    return render_template(
        "editarAtividade.html",
        usuario=usuario,
        atividade=atividade,
        codAtividade=codAtividade,
    )


@app.route("/atualizarAtividade/<int:codAtividade>", methods=["POST"])
def atualizarAtividade(codAtividade):
    # Obtém novos dados da atividade do formulário
    nomeAtividade = request.form["nomeAtividade"]
    descricaoAtividade = request.form["descricaoAtividade"]
    pesoAtividade = request.form["pesoAtividade"]
    dataAtividade = request.form["dataAtividade"]
    
    # Atualiza a atividade no banco de dados
    bd.atualizarAtividade(
        codAtividade, nomeAtividade, descricaoAtividade, dataAtividade, pesoAtividade
    )
    return redirect("/turmas")


if __name__ == "__main__":
    app.run(debug=True)
