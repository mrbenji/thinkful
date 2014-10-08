#!/usr/bin/env python

import authorization
import json
import requests
import sys, argparse
import logging

from urls import *

# Set the log output file, and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)


#def get(name, filename):
#    """ Print a snippet from a CSV file, based on an associated name. """
#    logging.info("Reading {} from {}".format(name, filename))
#    logging.debug("Opening a file")
#    with open(filename, "r") as f:
#        reader = csv.reader(f)
#        logging.debug("Reading snippet from file")
#        for line in reader:
#            logging.debug("line (list) = {}".format(line))
#            for key in line:
#                if key == name:
#                    logging.debug("Read successful")
#                    return name, line[1]
#    return name, None

def get_friends(auth):
    response = requests.get(GET_FRIENDS_URL, auth=auth)
    for user in response.json()["users"]:
        print user["screen_name"]
    #x = response.json()
    #print x["users"][0]
    #print json.dumps(response.json(), indent=4)


def get_followers(auth):
    response = requests.get(GET_FOLLOWERS_URL, auth=auth)
    print json.dumps(response.json(), indent=4)


def get_timeline(auth):
    response = requests.get(TIMELINE_URL, auth=auth)
    print json.dumps(response.json(), indent=4)


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

    if arguments['info']:
        if arguments['info'] == "friends":
            get_friends(auth)

        if arguments['info'] == "timeline":
            get_timeline(auth)

#    response = requests.get(TIMELINE_URL, auth=auth)
#    response = requests.get(GET_FRIENDS_URL, auth=auth)
#    print json.dumps(response.json(), indent=4)


if __name__ == "__main__":
    main()
