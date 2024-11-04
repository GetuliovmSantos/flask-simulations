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


if __name__ == "__main__":
    app.run(debug=True)
