import requests
import json
import csv

endpoints = {
  "people": "https://swapi.dev/api/people/",
  "planets": "https://swapi.dev/api/planets/",
  "films": "https://swapi.dev/api/films/",
  "species": "https://swapi.dev/api/species/",
  "vehicles": "https://swapi.dev/api/vehicles/",
  "starships": "https://swapi.dev/api/starships"
}

for k in endpoints:
  # Make a connection to the API
  request_api = requests.get(endpoints[k])
  # Pull data from the API
  pulled_data = request_api.text
  # Parse data into JSON format
  data_as_json = json.loads(pulled_data)
  # Extract detailed data
  data =data_as_json['results']

  # ** Create Appropriate CSV files per data set **

  # Open a file to write to
  data_file = open(f'starwars_{k}.csv', 'w')
  # Create a writer object
  csv_writer = csv.writer(data_file)

  # Create a counter to develop headers for the csv file
  counter = 0

  for value in data:
    # Create headers
    if counter == 0:
      header = value.keys()
      csv_writer.writerow(header)
      counter += 1

    # Write detailed data to csv
    csv_writer.writerow(value.values())

  #Close the writer file & reset the counter
  data_file.close()
  counter = 0