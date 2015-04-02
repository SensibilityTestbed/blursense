"""
Usage: python removeredundant.py filename
filename is the file to compress

"""

import subprocess
import sys

infile = sys.argv[1]
tempfile = 'tmp.txt'
p1 = subprocess.Popen(['cp', infile, tempfile], stdout=subprocess.PIPE)
output = p1.communicate()[0]

places = ['school', 'park', 'hotel', 'motel', 'resort', 'canyon', 'lake', 'inn', 'spring', 'mine', 'hall', 'canal', 'beach', 'suite', 'peak', 'ridge', 'saddle', 'station', 'gulch', 'laboratory', 'falls', 'memorial', 'heliport', 'transport', 'university', 'college', 'division', 'wilderness', 'reservoir', 'wharf', 'department', 'cemetery', 'mausoleum', 'siding', 'office', 'service', 'museum', 'bus stop', 'library', 'building', 'campus', 'campground', 'camping', 'campsite', 'shopping', 'plaza', 'zoo', 'hospital', 'travelodge', 'super 8', 'ritz', 'best western', 'sheraton', 'hilton', 'marriott', '\-AM', '\-FM', '\-TV']

placesw = ['sport', 'sports', 'slough', 'mount', 'county', 'estates', 'mill', 'house', 'lodge', 'creek', 'mountain', 'arena', 'auditorium', 'winery', 'lateral', 'crossing', 'reserve', 'field', 'westin', 'crag', 'crags', 'historical', 'pass', 'cabin', 'cabins', 'court', 'courtyard', 'club', 'dam', 'ranch', 'camp', 'place', 'downtown', 'marsh', 'church', 'flat', 'meadow', 'meadows', 'preserve', 'rock', 'mall', 'center', 'centers', 'trail', 'trails', 'trailer', 'trailhead', 'airport', 'bar', 'grove', 'gate', 'area', 'district', 'forest', 'home', 'homes', 'chapel', 'street', 'road', 'pit', 'ditch', 'drain', 'farm', 'bay', 'river', 'fall', 'quarry', 'hill', 'golf', 'plant', 'tunnel', 'terminal', 'academy', 'harbor', 'company', 'run', 'terrace', 'hyatt', 'ramada']

for p in places:
  print p
  cmd = 'grep -iv "' + p + '" tmp.txt > temp && mv temp tmp.txt'
  output, error = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  if error:
    print error
    continue
  
for p in placesw:
  print p
  cmd = 'grep -ivw "' + p + '" tmp.txt > temp && mv temp tmp.txt'
  output, error = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
  
subprocess.call(['ls', '-l'])
