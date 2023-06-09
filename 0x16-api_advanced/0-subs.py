#!/usr/bin/python3
"""
A function to query the Reddit API and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        int: The number of subscribers for the given subreddit. Returns 0 if the subreddit is not found or an error occurs.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
