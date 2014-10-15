#!/usr/bin/env python

from __future__ import unicode_literals
import authorization
import json
import requests
import sys, argparse
import logging

from urls import *

# Set the log output file and log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


def get_friends(auth):
    response = requests.get(GET_FRIENDS_URL, auth=auth)
    for user in response.json()["users"]:
        print user["screen_name"]


def get_followers(auth):
    response = requests.get(GET_FOLLOWERS_URL, auth=auth)
    for user in response.json()["users"]:
        print user["screen_name"]


def get_timeline(auth):
    response = requests.get(TIMELINE_URL, auth=auth)
    for post in response.json():
        post_string =  "\n" + post["user"]["screen_name"] + ": "
        post_string = post_string + post["text"].encode('ascii', 'ignore')
        post_string = post_string.replace("&amp;","&")
        print post_string

    #print json.dumps(response.json(), indent=4)

def post_status(status, auth):
    payload = {'status':status}
    requests.post(POST_STATUS_URL, auth=auth, params=payload)


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Command line Twitter client"
    parser = argparse.ArgumentParser(description=description)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--info', type=str, choices=["followers", "friends", "timeline"],
                       help="Display user information")
    group.add_argument('-t', '--tweet', type=str, help="Text to tweet")

    return parser


def main():
    """ Main function """
    logging.info("Tweetful -- starting main()")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)

    auth = authorization.authorize()

    if arguments['tweet']:
        print 'Tweeting "{}"'.format(arguments['tweet'])
        post_status(format(arguments['tweet']), auth)

    if arguments['info']:
        if arguments['info'] == "friends":
            get_friends(auth)

        if arguments['info'] == "followers":
            get_followers(auth)

        if arguments['info'] == "timeline":
            get_timeline(auth)

#    response = requests.get(TIMELINE_URL, auth=auth)
#    response = requests.get(GET_FRIENDS_URL, auth=auth)
#    print json.dumps(response.json(), indent=4)


if __name__ == "__main__":
    main()
