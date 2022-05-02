from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello", methods=["POST"])
def login():
	name = request.form.get("nombre")
	apellido = request.form.get("apellido")
	nacionalidad = request.form.get("nacionalidad")
	residencia = request.form.get("residencia")
	año = request.form.get("año")
	mes = request.form.get("Mes")
	dia = request.form.get("dia")
	profesion = request.form.get("profesion")
	estado = request.form.get("estado")
	usuario= request.form.get("usuario")
	return render_template(
		"session.html",
		name=name,
		apellido=apellido,
		nacionalidad=nacionalidad,
		residencia=residencia,
		año=año,
		mes=mes,
		dia=dia,
		profesion=profesion,
		estado=estado,
        usuario=usuario,
		)