#!/usr/bin/python3
""" returns top ten titles of given subreddit """

import requests


def top_ten(subreddit):
    """ print top ten post of a subreddit """
    url = "https://www.reddit.com/r/" + subreddit + "/top/.json"
    r = requests.get(url,
                     headers={'User-agent': 'norman'},
                     params={"limit": 10},
                     allow_redirects=False)
    if r.status_code == 200:
        for dic in r.json().get('data').get('children'):
            print(dic.get('data').get('title'))
    else:
        print("None")
