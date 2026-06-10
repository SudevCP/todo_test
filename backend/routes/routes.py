from flask import Blueprint, request, jsonify

from database.db import todos

todo_bp = Blueprint("todo", __name__)

@todo_bp.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@todo_bp.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    task = data.get("task")

    if not task:
        return jsonify({"error; Task is required"}), 400
    
    new_id = max((todo["id"] for todo in todos), default=0) + 1
    
    todo = {
        "id": new_id,
        "task": task
    }
    todos.append(todo)

    return jsonify(todo), 201

@todo_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return jsonify({"message": "Todo deleted successfully"}), 200

    return jsonify({"error": "Todo not found"}), 404