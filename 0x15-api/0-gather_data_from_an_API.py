#!/usr/bin/python3
'''
A Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
'''
import requests
from sys import argv


def get_info(employee_id):
    '''
    The function to retrieve employee information.
    '''
    emp_id = argv[1]
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(emp_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(emp_id)).json()
    name = emp.get('name')
    count = 0
    completed_tasks = []
    completed_count = 0
    for todo in todos:
        count += 1
        if todo.get('completed'):
            completed_tasks.append(todo.get('title'))
            completed_count += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_count, count))
    for task in completed_tasks:
        print('\t {}'.format(task))


if __name__ == "__main__":
    get_info(int(argv[1]))
