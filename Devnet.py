from requests import get
import json
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.geocoders import Nominatim
import time

app = Nominatim(user_agent="tutorial")
ip = get('https://ip4.seeip.org').text
geo= get('https://ip.seeip.org/geoip').text
x = json.loads(geo)
response = DbIpCity.get(ip, api_key='free')

ipv6 = get('https://ip.seeip.org').text

def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    coordinates = f"{latitude}, {longitude}"
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

address = get_address_by_location(response.latitude, response.longitude, language="en")
lat = str(response.latitude)
lng = str(response.longitude)

print("Location of IP :" + address)

# print(address['display_name'])


print("IPv4 IP address : " + ip)

print("IPv6 IP address : " + ipv6)

for key in x:
    print(key, " : " , x[key])




