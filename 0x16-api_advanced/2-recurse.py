#!usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit
import requests
"""

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        hot_list (list, optional): The list to store the titles of the hot articles. Defaults to an empty list.

    Returns:
        list or None: A list containing the titles of all hot articles for the given subreddit,
                      or None if the subreddit is not found.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Custom User Agent"}  # Add your custom User-Agent here

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        if data["data"]["after"]:
            # If there is a "after" value in the response, call the function recursively with the updated URL
            new_url = url + f"&after={data['data']['after']}"
            recurse(subreddit, hot_list, new_url)

    elif response.status_code == 404:
        # If the subreddit is not found, return None
        return None

    return hot_list
