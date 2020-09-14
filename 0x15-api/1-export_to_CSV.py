#!/usr/bin/python3
""" fetch data from api and display it """

import csv
import requests
import sys


if __name__ == "__main__":
    api_todos = "https://jsonplaceholder.typicode.com/users/"\
                + sys.argv[1] + "/todos"
    api_user = "https://jsonplaceholder.typicode.com/users/"\
               + sys.argv[1]
    file_name = sys.argv[1] + ".csv"
    r1 = requests.get(api_todos)
    r2 = requests.get(api_user)
    user_name = r2.json().get("username")
    with open(file_name, mode="w", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in r1.json():
            writer.writerow([str(item.get("userId")),
                            user_name, str(item.get("completed")),
                            item.get("title")])
