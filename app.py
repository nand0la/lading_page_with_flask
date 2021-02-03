from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'simple_lading_page'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form-headler", methods=["POST", "GET"])
def form_submit():

    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':   
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        cursor = mysql.connection.cursor()
        cursor.execute("""INSERT INTO users(nome, email, telefone) VALUES(%s,%s,%s)""",(nome, email, telefone))
        mysql.connection.commit()
        cursor.close()

        return f"enviado"


app.run(debug=True)