from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

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
    return response

@app.route('/eventos')
def eventos():
    datos = {
        "eventos": [
            {
                "dia": "10",
                "mes": "MAY",
                "titulo": "Torneo de tenis — inscripciones abiertas",
                "descripcion": "Torneo interno mensual en canchas de polvo de ladrillo. Categorías: primera, segunda y damas.",
                "categoria": "Deporte"
            },
            {
                "dia": "14",
                "mes": "MAY",
                "titulo": "Corte de agua programado",
                "descripcion": "Mantenimiento de red hídrica. Sin suministro de 9 a 13hs en sector norte.",
                "categoria": "Aviso"
            },
            {
                "dia": "18",
                "mes": "MAY",
                "titulo": "Feria de productores — Club House",
                "descripcion": "Feria mensual con productores locales. Frutas, verduras y productos artesanales.",
                "categoria": "Comunidad"
            },
            {
                "dia": "24",
                "mes": "MAY",
                "titulo": "Clases de kayak — inicio de temporada",
                "descripcion": "Clases grupales para todas las edades en el lago. Inscripción previa requerida.",
                "categoria": "Deporte"
            }
        ]
    }
    response = jsonify(datos)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
