from flask import Flask, render_template, request, redirect, url_for, session, flash, g, abort
import sqlite3

app = Flask("_name_")

# POSTS MOCK

posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro post"
    },
    {
        "titulo": "Post 2",
        "texto": "Olha eu aqui de novo"
    }
]

# USER MOCKS
USERNAME = "admin"
PASSWORD = "admin"
DATABASE = "blog.bd"

@app.before_request
def pre_requisicao():
    g.bd = conectar_bd()

@app.teardown_request
def encerrar_requisicao(exception):
    g.bd.close()

@app.route("/")
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas = posts) 

@app.route('/login', methods = ["GET", "POST"])
def login ():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSwORD:
            return "dados recebidos"
    return render_template("login.html")


