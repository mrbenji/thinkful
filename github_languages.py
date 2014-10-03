import sys

from secret import USERNAME, PASSWORD

PROXY = False

if PROXY:
    from secret import PROXIES
    VERIFY = False
else:
    PROXIES = None
    VERIFY = True

import requests

def get_repositories(user):
    """ Retreive a list of a user's repositories """
    url = "https://api.github.com/users/{user}/repos".format(user=user)
    response = requests.get(url, auth=(USERNAME, PASSWORD), proxies=PROXIES, verify=VERIFY)
    return response.json()

def get_language_dictionaries(repositories):
    """
    Return a list of dictionaries containing the languages used in each
    repository
    """
    language_dictionaries = []
    for repository in repositories:
        url = "https://api.github.com/repos/{owner}/{repo}/languages"
        url = url.format(owner=repository["owner"]["login"],
                         repo=repository["name"])
        response = requests.get(url, auth=(USERNAME, PASSWORD), proxies=PROXIES, verify=VERIFY)
        language_dictionaries.append(response.json())
    return language_dictionaries

def main():
    """ Main function """
    repositories = get_repositories(sys.argv[1])
    language_dictionaries = get_language_dictionaries(repositories)
    print language_dictionaries


if __name__ == "__main__":
    main()

