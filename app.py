from flask import Flask, jsonify, abort

days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)


@app.route("/<int:day_id>", methods=["GET"])
def get_day(day_id):
    day = [day for day in days if day["id"] == day_id]
    if len(day) == 0:
        abort(404)
    return jsonify({"day": day[0]})


@app.route("/name/<string:day_name>", methods=["GET"])
def get_day_by_name(day_name):
    day = [day for day in days if day["name"].lower() == day_name.lower()]
    if not day:
        abort(404)
    return jsonify({"day": day[0]})

#
@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201

@app.route('/saludo', methods=['POST'])
def saludo():
    data = get_days
    nombre = data.get('nombre')
    return jsonify({'mensaje': f'¡Hola, {nombre}!'})
if __name__ == "__main__":
    app.run(debug=True)
