from flask import Flask, render_template, request, redirect
from bd import BD

app = Flask(__name__)
bd = BD()
usuario = None


@app.route("/")
def index():
    connection = bd.connect()

    if "error" in str(connection):
        return render_template("index.html", error=connection["error"])

    bd.close()

    return render_template("index.html", error=None)


@app.route("/logar", methods=["POST"])
def logar():
    global usuario

    login = request.form["login"]
    senha = request.form["senha"]
    usuario = bd.login(login, senha)
    if "error" in usuario:
        return render_template("index.html", error=usuario["error"])
    else:
        return redirect("/turmas")


@app.route("/esqueciSenha")
def esqueciSenha():
    return render_template("esqueciSenha.html", error=None)


@app.route("/recuperarSenha", methods=["POST"])
def recuperarSenha():
    login = request.form["login"]
    senha = request.form["senha"]
    cSenha = request.form["cSenha"]

    result = bd.recuperarsenha(login, senha, cSenha)

    if "error" in result:
        return render_template("esqueciSenha.html", error=result["error"])
    else:
        return redirect("/")


@app.route("/turmas")
def turmas():
    turmas = bd.buscarTurmas(usuario["loginUsuario"])

    return render_template("turmas.html", usuario=usuario, turmas=turmas)


@app.route("/adicionarTurma")
def adicionarTurma():
    return render_template("adicionarTurma.html", usuario=usuario)


@app.route("/salvarTurma", methods=["POST"])
def salvarTurma():
    nomeTurma = request.form["nomeTurma"]
    periodoTurma = request.form["periodoTurma"]
    bd.salvarTurma(usuario["loginUsuario"], nomeTurma, periodoTurma)

    return redirect("/turmas")


@app.route("/excluirTurma/<int:codTurma>")
def excluirTurma(codTurma):
    bd.excluirTurma(codTurma)
    return redirect("/turmas")


@app.route("/adicionarAtividade/<int:codTurma>")
def adicionarAtividade(codTurma):
    return render_template(
        "adicionarAtividade.html", usuario=usuario, codTurma=codTurma
    )


@app.route("/salvarAtividade/<int:codTurma>", methods=["POST"])
def salvarAtividade(codTurma):
    nomeAtividade = request.form["nomeAtividade"]
    descricaoAtividade = request.form["descricaoAtividade"]
    pesoAtividade = request.form["pesoAtividade"]
    dataAtividade = request.form["dataAtividade"]
    bd.salvarAtividade(
        nomeAtividade, descricaoAtividade, dataAtividade, pesoAtividade, codTurma
    )
    return redirect("/turmas")


@app.route("/verAtividades/<int:codTurma>")
def verAtividades(codTurma):
    atividades = bd.buscarAtividades(codTurma)
    return render_template(
        "verAtividades.html", usuario=usuario, atividades=atividades, codTurma=codTurma
    )

@app.route("/excluirAtividade/<int:codAtividade>")
def excluirAtividade(codAtividade):
    bd.excluirAtividade(codAtividade)
    return redirect("/turmas")

@app.route("/editarAtividade/<int:codAtividade>")
def editarAtividade(codAtividade):
    atividade = bd.buscarAtividade(codAtividade)
    return render_template("editarAtividade.html", usuario=usuario, atividade=atividade, codAtividade=codAtividade)

@app.route("/atualizarAtividade/<int:codAtividade>", methods=["POST"])
def atualizarAtividade(codAtividade):
    nomeAtividade = request.form["nomeAtividade"]
    descricaoAtividade = request.form["descricaoAtividade"]
    pesoAtividade = request.form["pesoAtividade"]
    dataAtividade = request.form["dataAtividade"]
    bd.atualizarAtividade(codAtividade, nomeAtividade, descricaoAtividade, dataAtividade, pesoAtividade)
    return redirect("/turmas")


if __name__ == "__main__":
    app.run(debug=True)
