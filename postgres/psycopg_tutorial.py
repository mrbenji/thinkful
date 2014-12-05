#!/usr/bin/env python
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
    conn = psycopg2.connect("dbname='pets' user='codio' host='localhost' password=''")
except:
    print "I am unable to connect to the database"

curr = conn.cursor()

curr.execute("""SELECT datname from pg_database""")
rows = curr.fetchall()
for row in rows:
    print str(row)

