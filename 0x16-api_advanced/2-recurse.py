#!usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
"""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        hot_list (list): Optional. The list to store the titles of hot articles. Default is None.
        after (str): Optional. The pagination token for retrieving the next page of results. Default is None.

    Returns:
        list or None: A list containing the titles of all hot articles in the subreddit, or None if the subreddit is not found or an error occurs.
    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Custom User Agent"}  # Add your custom User-Agent here
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
