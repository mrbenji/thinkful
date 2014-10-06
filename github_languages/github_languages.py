#!/usr/bin/env python

import sys
import operator
from collections import defaultdict
from secret import USERNAME, PASSWORD

PROXY = False

if PROXY:
    from secret import PROXIES
    VERIFY = False
else:
    PROXIES = None
    VERIFY = True

import requests

def accumulate_languages(language_dictionaries):
    """ Calculate the total data size for each language """
    accumulated = defaultdict(int)
    total = 0
    for language_dictionary in language_dictionaries:
        for language_name, number_of_bytes in language_dictionary.iteritems():
            accumulated[language_name] += number_of_bytes
            total += number_of_bytes
    return accumulated, total


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
    language_totals, total_bytes = accumulate_languages(language_dictionaries)

    sorted_language_totals = sorted(language_totals.iteritems(),
                                    key=operator.itemgetter(1),
                                    reverse=True)

    for language_name, number_of_bytes in sorted_language_totals:
        percentage = 100.0 * number_of_bytes / total_bytes
        print "{}: {:.2f}%".format(language_name, percentage)


if __name__ == "__main__":
    main()

