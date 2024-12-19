from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database to check all tasks
'''Tasks will have a
Name: User typed in to specify WHAT the task is, string
ID: Unique system implemented ID, int
Complete: Contains boolean value
'''
tasks = []

# Route to get all tasks using GET method
@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(tasks), 200

# Add task to task manager using POST method
@app.route("/tasks", methods = ["POST"])
def add_task():
    data = request.get_json() # parses requested data and stores in Python dictionary
    # With the data object, .get() to find name of task and implement it into dictionary
    new_task = {
        "name": data.get("name"),
        "id": len(tasks) + 1,
        "complete": False
    }
    tasks.append(new_task) # Append new task to Virtual database
    return jsonify(new_task), 201

# Modify task in task manager given task id using PUT method
@app.route("/tasks/int:<id>", methods = {"PUT"})
def modify_task(id):
    data = request.get_json()
    for task in tasks:
        if tasks["id"] == id:
            task["name"] = data.get("name", task["name"])
            task["completed"] + data.get("completed", task["completed"])
            return jsonify(task), 200
    return print("Error: Task not found"), 404