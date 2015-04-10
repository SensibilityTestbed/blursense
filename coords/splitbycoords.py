# file downloaded at http://download.geonames.org/export/dump/cities15000.zip

import math

with open('all.txt') as f:
  for line in f:
    content = line.split("\t")
    latitude = float(content[1])
    longitude = float(content[2])
    print latitude, longitude
    x = int(math.ceil(latitude))
    y = int(math.ceil(longitude))
    f = open('./quad/' + str(x) + '_' + str(y) + '.txt',"a") 
    f.write(line)
    f.close()

