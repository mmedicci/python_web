from flask import Flask, render_template

app = Flask("_name_")

# POSTS MOCK

posts = [
    {
        "titulo": "Post 1",
        "text": "Meu primeiro post"
    },
    {
        "titulo": "Post 2",
        "text": "Olha eu aqui de novo"
    }
]

@app.route("/")
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas = posts) 

