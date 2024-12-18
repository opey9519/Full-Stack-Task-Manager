from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary database to check all tasks
tasks = []

# Route to get all tasks
@app.route("/tasks", methods = ["GET"])
def get_tasks():
    return jsonify(tasks), 200