#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='pets' user='codio' host='localhost' password=''")
except:
    print "I am unable to connect to the database"