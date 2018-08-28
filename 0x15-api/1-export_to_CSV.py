#!/usr/bin/python3
'''
A Python script that, using this REST API,
for a given employee ID, exports data in the CSV format.
'''
import csv
import requests
from sys import argv


def output_csv(employee_id):
    '''
    The function to retrieve employee information.
    '''
    emp_id = argv[1]
    emp = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(emp_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(emp_id)).json()
    csvfile = emp_id + '.csv'
    with open(csvfile, 'w', newline='') as output:
        tasks = csv.writer(output, quoting=csv.QUOTE_ALL)
        for todo in todos:
            tasks.writerow([emp_id, emp.get('username'),
                           todo.get('completed'), todo.get('title')])


if __name__ == "__main__":
    output_csv(int(argv[1]))
