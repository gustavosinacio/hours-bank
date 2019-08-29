#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect(database="hours", host='localhost', user="postgres", password='postgres')
cur = conn.cursor()

# cur.execute("INSERT INTO dates (timedate_in) VALUES (convert(datetime, '19-08-05 12:30:00 AM',5))")
cur.execute("INSERT INTO timedate_in ")

conn.commit()

cur.close()
conn.close()