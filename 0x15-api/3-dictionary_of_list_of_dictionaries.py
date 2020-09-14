#!/usr/bin/python3
""" fetch data from api and display it """

import json
import requests
import sys


if __name__ == "__main__":
    api_users = "https://jsonplaceholder.typicode.com/users/"
    file_name = "todo_all_employees.json"
    dic = {}
    lista = []
    r2 = requests.get(api_users)
    for user in r2.json():
        api_todos = "https://jsonplaceholder.typicode.com/users/"\
          + str(user.get("id")) + "/todos"
        r1 = requests.get(api_todos)
        for item in r1.json():
            lista.append({"task": item.get("title"),
                          "completed": item.get("completed"),
                          "username": user.get("username")})
        dic[user.get("id")] = lista
        lista = []
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(dic))
