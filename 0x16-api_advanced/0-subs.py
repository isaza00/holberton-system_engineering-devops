#!/usr/bin/python3
""" returns number of subscribers of reddi api """

import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers of subredit """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    r = requests.get(url, headers={'User-agent': 'norman'},
                     allow_redirects=False)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
