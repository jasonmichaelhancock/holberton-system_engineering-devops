#!/usr/bin/python3
'''
A function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
'''

import requests


def top_ten(subreddit):
    '''Prints the titles of the first 10 hot posts on r/`subreddit`'''
    endpoint = 'https://reddit.com/r/{}.json'.format(subreddit)
    user = {'User-Agent': 'x'}

    r = requests.get(endpoint, headers=user).json()
    try:
        hot_posts = r.get('data').get('children')
    except AttributeError:
        print('None')
        return
    i = 0
    for post in hot_posts:
        if i < 10:
            print(post.get('data').get('title'))
        i += 1
