#!/usr/bin/python3
'''
A Python script that, using this REST API,
for all employee IDs, exports data in the json format.
'''
import json
import requests
from sys import argv


def output_json():
    '''
    The function to retrieve employee information.
    '''
    jsonfile = 'todo_all_employees.json'
    emps = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    all_emps = {}
    current_emp = {}
    for emp in emps:
        emp_id = emp.get('id')
        all_emps[emp_id] = []
        current_emp[emp_id] = emp.get('username')
    for todo in todos:
        task = {}
        emp_id = todo.get('userId')
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = current_emp.get(emp_id)
        all_emps.get(emp_id).append(task)
        with open(jsonfile, 'w') as output:
            json.dump(all_emps, output)

if __name__ == "__main__":
    output_json()
