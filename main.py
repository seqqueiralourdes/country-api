from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def country_app():
    
    datos = {
        "avisos": [
            "Corte de agua mañana a las 8hs",
            "Reunión de consorcio el viernes",
            "Mantenimiento de espacios verdes el lunes"
        ],
        "expensas": {
            "estado": "Al día",
            "monto": 15000,
            "vencimiento": "10/05/2026"
        }
    }

   response = jsonify(datos)
response.headers.add('Access-Control-Allow-Origin', '*')
app.config['JSON_AS_ASCII'] = False
return response

if __name__ == '__main__':
    app.run(debug=True)
