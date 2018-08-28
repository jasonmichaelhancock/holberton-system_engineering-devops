#!/usr/bin/python3
'''
A Python script that, using this REST API,
for a given employee ID, exports data in the json format.
'''
import json
import requests
from sys import argv


def output_json(employee_id):
    '''
    The function to retrieve employee information.
    '''
    emp_id = argv[1]
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(emp_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()
    jsonfile = emp_id + '.json'
    todo_list = []
    for todo in todos:
        task = {}
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = emp.get('username')
        todo_list.append(task)
    json_todos = {}
    json_todos[emp_id] = todo_list
    with open(jsonfile, 'w') as output:
        json.dump(json_todos, output)


if __name__ == "__main__":
    output_json(int(argv[1]))
