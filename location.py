import sys
import math
import struct
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng

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
        geolocator = GoogleV3();
        loc = geolocator.geocode(name)
        return self.move_to_cord(loc.latitude, loc.longitude, loca.altitude)

    def move_to_cord(self, lat, lon, alt):
        return 1

    def get_adj_cell_id(self, radius=20):
        start = CellId.from_lat_lng(
                LatLng.from_degrees(self.lat,
                    self.lon)
                ).parent(15)

        ids = [start.id()]
        nxt = start.next()
        prv = start.prev()
        for _ in range(radius):
            ids.append(nxt.id())
            ids.append(prv.id())
            nxt = nxt.next()
            prv = prv.prev()

        print(ids)
        return ids



def utils_f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]





