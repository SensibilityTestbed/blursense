import random
import math
import os.path
    
def get_coordinates():
  lat = random.uniform(-90.0, 90.0)
  lng = random.uniform(-180.0, 180.0)
  return [lat, lng]


def get_filename(latitude, longitude):
  # get ceiling as x/y index
  x = int(math.ceil(latitude))
  y = int(math.ceil(longitude))
  filename = './quad/' + str(x) + '_' + str(y) + '.txt'
  if os.path.isfile(filename):
    return filename
  else:
    return None

  
def load_lat_long_from_file(filename):
  listofpoints = {}
  with open(filename) as fp:
    for line in fp:
      line = line.strip()
      data = line.split("\t")
      try:
        city_name = data[0]
        lat = float(data[1])
        lng = float(data[2])
        country = data[3]
        state = data[4]
      except IndexError:
        # sometimes certain field can be missing from file
        pass
      else:
        listofpoints[city_name] = [lat, lng, country, state]
      
  for p in listofpoints:   
    print p, listofpoints[p]
  
  return listofpoints

def find_distance(p1, p2):
  (lat1, lng1) = p1
  (lat2, lng2) = p2
  lat_diff = (lat1-lat2) * (lat1-lat2)
  lng_diff = (lng1-lng2) * (lng1-lng2)
  # return squared distance
  return lat_diff + lng_diff

def find_closest_point(latitude, longitude, listofpoints):
  min_dist = 9999
  closest_point = ()
  point1 = (latitude, longitude)
  closest_city = ""
  country = ""
  state = ""
  
  cities = listofpoints.keys()
  for city in cities:
    data = listofpoints[city]
    point2 = (data[0], data[1])
    dist = find_distance(point1, point2)
    if dist < min_dist:
      min_dist = dist
      closest_point = point2
      closest_city = city
      state = data[3]
      country = data[2]

  return {"city": closest_city, "state": state, "country": country, "coordinates": closest_point}

while True:      
  [latitude, longitude] = get_coordinates() #[-21.0197317515, 55.8750057031] 
  filename = get_filename(latitude, longitude)

  if filename != None:
    print str(latitude) + ', ' + str(longitude) + ' is around\n'
    listofpoints = load_lat_long_from_file(filename)
    print "\nclosest point:", find_closest_point(latitude, longitude, listofpoints)
    break

