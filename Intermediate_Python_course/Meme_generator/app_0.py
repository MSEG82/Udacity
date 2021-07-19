from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def saludo():
    return "que tal?"

if __name__ == "__main__":
    app.run()
