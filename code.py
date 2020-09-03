import os
from datetime import datetime, timedelta
import ast
import dateutil.parser

import re 
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--json_filepath', nargs=1,type=argparse.FileType('r'))
parser.add_argument('--created_before', type=int)
parser.add_argument('--prefix', type=str)
mynamespace = parser.parse_args()
created_before = mynamespace.created_before
prefix_str = mynamespace.prefix
# json_path = mynamespace.json_filepath
# there was some issue while passing json-filepath, therefore user input for this. 
json_path = input("Please enter json file path")

data = []
count = 0 
str_count = 0 
with open(json_path, "r") as inFile:
    data = ast.literal_eval(inFile.read())
    for row in data:
        diff = (datetime.now() - dateutil.parser.parse(row['creationTimestamp']).replace(tzinfo=None)) 
        if diff >  timedelta(days=created_before):
            count += 1
        if re.search(f"^{prefix_str}", row['name']) and (diff >  timedelta(days=created_before)):
            str_count += 1    

print(f"Total number of images older than {created_before} days {count}")
print(f"Total number of images with prefix ccops older than {created_before} days : {str_count}")
