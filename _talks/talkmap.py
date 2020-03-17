

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: Path, getorg, geopy

from pathlib import Path
import getorg
from geopy import Nominatim

geocoder = Nominatim(user_agent='github-generator')
location_dict = {}
location = ""
permalink = ""
title = ""

# check files for location tags
for file in Path('_talks').glob('**/*.md'):
    print(file)
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
                            
        location_dict[location] = geocoder.geocode(location)
        print("location: ", location, "\n", location_dict[location])

# save locations
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)




