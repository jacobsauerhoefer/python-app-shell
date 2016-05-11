#!/usr/bin/env python
""" Module Comment """

from flask import jsonify, Blueprint

task_api = Blueprint(
    'task_api', __name__
)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@task_api.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """ Function Comment """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return
        # abort(404)
    return jsonify({'task': task[0]})
