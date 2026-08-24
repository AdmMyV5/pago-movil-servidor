from flask import Flask, request, jsonify, render_template_string
from datetime import datetime

app = Flask(__name__)

pagos = []


@app.route("/")
def inicio():
    html = """
    <html>
    <head>
        <title>Pago Móvil Bot</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial;
                background:#f2f2f2;
                padding:20px;
            }
            .card {
                background:white;
                padding:15px;
                margin:10px;
                border-radius:10px;
                box-shadow:0 0 5px #aaa;
            }
        </style>
    </head>

    <body>

    <h1>Pago Móvil Bot</h1>
    <h3>Pagos recibidos Bancamiga</h3>

    {% for p in pagos %}

    <div class="card">
        <b>Banco:</b> {{p.banco}} <br>
        <b>Teléfono:</b> {{p.telefono}} <br>
        <b>Monto:</b> {{p.monto}} <br>
        <b>Mensaje:</b> {{p.mensaje}} <br>
        <small>{{p.fecha}}</small>
    </div>

    {% endfor %}

    </body>
    </html>
    """

    return render_template_string(html, pagos=pagos)


@app.route("/recibir", methods=["POST"])
def recibir():

    datos = request.json

    pago = {
        "banco": datos.get("banco"),
        "telefono": datos.get("telefono"),
        "monto": datos.get("monto"),
        "mensaje": datos.get("mensaje"),
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    pagos.append(pago)

    print("PAGO RECIBIDO:")
    print(pago)

    return jsonify({
        "estado":"ok"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
