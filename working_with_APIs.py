import requests
import json
import csv
import os

# Make a connection to the Requests API
response_API = requests.get('https://swapi.dev/api/people/')
# Pull data from the API
json_data = response_API.text
# Parse the data into JSON format
parse_json = json.loads(json_data)
# Drill down to the desired set of data from the API
starwars_names = parse_json['results']

# Print to console
#print(starwars_names)

# Write data to a csv

# Open a file to write to
csv_file = open('starwars_names.csv', 'w')

# CSV writer object
csv_writer = csv.writer(csv_file)

# Used for headers
count = 0

for name in starwars_names:
  if count == 0:
    #Headers
    header = name.keys()
    csv_writer.writerow(header)
    count +=1

  #CSV data
  csv_writer.writerow(name.values())

# Close file
csv_file.close()
