from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados (base de datos en memoria)
users = {
    "1": {"id": "1", "name": "practica", "telefono": "991-982-123"},
}

@app.route("/")
def root():
    return "Home"


# ---------- GET ----------
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    query = request.args.get("query")
    if query:
        user = user.copy()
        user["query"] = query

    return jsonify(user), 200


# ---------- POST ----------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "id" not in data or "name" not in data or "telefono" not in data:
        return jsonify({"error": "Datos incompletos"}), 400

    user_id = data["id"]
    if user_id in users:
        return jsonify({"error": "El usuario ya existe"}), 409

    users[user_id] = data
    return jsonify({"message": "Usuario creado", "user": data}), 201


# ---------- PUT ----------
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400

    users[user_id].update(data)
    return jsonify({"message": "Usuario actualizado", "user": users[user_id]}), 200


# ---------- DELETE ----------
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "Usuario no encontrado"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "Usuario eliminado", "user": deleted_user}), 200


if __name__ == "__main__":
    app.run(debug=True)