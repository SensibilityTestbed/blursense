# file downloaded at http://download.geonames.org/export/zip/allCountries.zip

import math

with open('states.txt') as f:
  for line in f:
    content = line.split(".")
    country = content[0]
    print country
    f = open('./states/' + str(country) + '.txt',"a") 
    f.write(line)
    f.close()

