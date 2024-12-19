from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database to check all tasks
'''Tasks will have a
Name: User typed in to specify WHAT the task is, string
ID: Unique system implemented ID, int
Complete: Contains boolean value
'''
tasks = []

# Route to get all tasks
@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(tasks), 200

# Add task to task manager
@app.route("/tasks", methods = ["POST"])
def add_task():
    data =request.get_json()
    new_task = {
        "name": data.get("name"),
        "id": len(tasks) + 1,
        "complete": False
    }
    return jsonify(new_task), 201