#!/usr/bin/python3
""" fetch data from api and display it """

import requests
import sys


if __name__ == "__main__":
    api_todos = "https://jsonplaceholder.typicode.com/users/"\
                + sys.argv[1] + "/todos"
    api_user = "https://jsonplaceholder.typicode.com/users/"\
               + sys.argv[1]
    tasks_done = 0
    r1 = requests.get(api_todos)
    r2 = requests.get(api_user)
    for task in r1.json():
        if task.get("completed") is True:
            tasks_done += 1
    print("Employee {} is done with tasks({}/{}):".
          format(r2.json().get("name"),
                 tasks_done,
                 len(r1.json())))
    for task in r1.json():
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
