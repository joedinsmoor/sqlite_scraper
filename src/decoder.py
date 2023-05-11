import re
import sqlite3
import string
from logger import *

'''
- Decode and remove extraneous hex data, leaving only ascii characters
- Send various scraped data to different logs and output files
- If image found, reconstruct image and save
- If phone number found, send to csv file
'''


def decode(cur):
    for row in cur.execute("SELECT data FROM object_data"):
     row_str = str(row)
     row_str_decoded = bytes(row_str, "utf-8").decode("unicode_escape")
     row_decoded = re.sub('r\\\\x[0-9a-fA-F]{2}', "", row_str_decoded)
     print_me = row_decoded.encode('ascii', 'ignore').decode('ascii')
     for i in re.findall(r'[\+\(]?[1-9][0-9 .\-(\)]{8,}[0-9]', print_me):
       phone_numbers(i)
     print(print_me)
     scraper_log(print_me)

