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


def make_parser():
    """ Construct the command line parser """
    logging.info("Constructing parser")
    description = "Command line Twitter client"
    parser = argparse.ArgumentParser(description=description)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', type=str, choices=["followers", "following"],
                       help="Display user information")
    group.add_argument('-t', '--text', type=str, help="Text to tweet")

#    subparsers = group.add_subparsers(dest="command", help="Available commands")
#
#    # Subparser for the tweet command
#    logging.debug("Constructing tweet subparser")
#    tweet_parser = subparsers.add_parser("tweet", help="Post a tweet")
#    tweet_parser.add_argument("text", help="Text to tweet")
#
#    # Subparser for the info command
#    logging.debug("Constructing info subparser")
#    info_parser = subparsers.add_parser("-i","--info", type=string, help="Display user info")
#    info_parser.add_argument("display_info", help="info to display")
#    info_parser.add_argument("following", help="List Twitter users followed")

    return parser


def main():
    """ Main function """
    logging.info("Tweetful -- starting main()")
    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)

    if arguments['t']:
        print 'Tweeting "{}"'.format(arguments['t'])

    if arguments['i']:
        print 'Info routine called with "{}"'.format(arguments['i'])

#    auth = authorization.authorize()

#    response = requests.get(TIMELINE_URL, auth=auth)
#    print json.dumps(response.json(), indent=4)


if __name__ == "__main__":
    main()
