import sys
import math
import struct
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3

class Location:
    lat = 0
    lon = 0
    alt = 0
    flat = 0
    flon = 0

    def set_location_cord(self, lat, lon, alt):
        self.flat = lat
        self.flon = lon
        self.lat = utils_f2i(lat)
        self.lon = utils_f2i(lon)
        self.alt = utils_f2i(alt)
        print('[LO]\tYou are now at '+str(self.lat) +","+str(+self.lon)+","+str(self.alt))
        return True


    def set_location_name(self, name):
        geolocator = GoogleV3()
        loc = geolocator.geocode(name)
        print('[LO]\tYou are not at '+ format(loc.address.encode('utf-8')))
        return self.set_location_cord(loc.latitude, loc.longitude, loc.altitude)

    def move_to_name(self, name):
        return 1

    def move_to_cord(self, lat, lon, alt):
        return 1


def utils_f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]


        


