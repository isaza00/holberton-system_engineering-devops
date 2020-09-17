#!/usr/bin/python3
""" returns hot post of given subreddit """

import requests


def recurse(subreddit, hot_list=[], after="None"):
    """ recursively return all hot post of subreddit """
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    r = requests.get(url,
                     headers={'User-agent': 'norman'},
                     params={"limit": 100, "after": after},
                     allow_redirects=False)
    if after is "fin" or after is None:
        return hot_list
    elif r.status_code == 200:
        for dic in r.json().get('data').get('children'):
            hot_list.append(dic.get('data').get('title'))
        after = r.json().get('data').get('after')
        if after is None:
            after = "fin"
        recurse(subreddit, hot_list, after=after)
    elif after == "None":
        return
    return hot_list
