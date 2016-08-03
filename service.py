import argparse
import sys
import location
import status
import api
import requests
import json
import re
import time

from POGOProtos.Networking.Requests import Request_pb2
from POGOProtos.Networking.Requests import RequestType_pb2
from POGOProtos.Networking.Envelopes import ResponseEnvelope_pb2
from POGOProtos.Networking.Envelopes import RequestEnvelope_pb2
from POGOProtos.Networking.Requests.Messages import EncounterMessage_pb2
from POGOProtos.Networking.Requests.Messages import FortSearchMessage_pb2
from POGOProtos.Networking.Requests.Messages import FortDetailsMessage_pb2
from POGOProtos.Networking.Requests.Messages import CatchPokemonMessage_pb2
from POGOProtos.Networking.Requests.Messages import GetInventoryMessage_pb2
from POGOProtos.Networking.Requests.Messages import GetMapObjectsMessage_pb2
from POGOProtos.Networking.Requests.Messages import EvolvePokemonMessage_pb2
from POGOProtos.Networking.Requests.Messages import ReleasePokemonMessage_pb2
from POGOProtos.Networking.Requests.Messages import UseItemCaptureMessage_pb2
from POGOProtos.Networking.Requests.Messages import DownloadSettingsMessage_pb2
from POGOProtos.Networking.Requests.Messages import UseItemEggIncubatorMessage_pb2
from POGOProtos.Networking.Requests.Messages import RecycleInventoryItemMessage_pb2
from POGOProtos.Networking.Requests.Messages import NicknamePokemonMessage_pb2

API_URL = 'https://pgorelease.nianticlabs.com/plfe/rpc'

# TODO -> Hide errors: From ### 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Service:
    def __init__(self, token=None, location_name=""):
        self.access_token = token
        self.origin_location = location_name
        self.authTicket = None

        # Create Niantic Session
        self.session = requests.session()
        self.session.headers = {
                'User-Agent': 'Niantic App'
                }
        self.session.verify = False

        self.state = None

        self.start_process(token, location_name)

    def restart_process(self):
        return 1


    def start_process(self, token, location_name=""):
        self.location = location.Location()
        self.location.set_location_name(location_name);     # Get Location at here
        print('[SE]\tGoogle token: '+ token[:40])

        self.state = status.Status() 
        self.endpoint = 'https://{0}{1}'.format(self.create_api_end_point(),'/rpc')

        payload = [Request_pb2.Request(request_type = RequestType_pb2.GET_PLAYER)]
        res = self.wrap_and_request(payload) 
        self.state.profile.ParseFromString(res.returns[0])

        print('[SE]\tHello, ' + self.state.profile.player_data.username)
        # print(self.state.eggs)        # Empty
        # print(self.state.inventory)   # Too much
        # print(self.state.badges)      # Empty
        # print(self.state.settings)    # Useless
        self.get_map_objects()

    def create_api_end_point(self):
        payload = []
        msg = Request_pb2.Request(request_type = RequestType_pb2.GET_PLAYER)
        payload.append(msg)
        req = self.wrap_in_request(payload)
        res = self.request(req, API_URL)
        if res is None:
            print("Servers are busy now. Exiting")
            sys.exit("Can't connect to server in creating api endpoint, Error 51263")
        return res.api_url

    def wrap_in_request(self, payload):
        info = None
        if not self.authTicket:
            info = RequestEnvelope_pb2.RequestEnvelope.AuthInfo(
                    provider = "google",
                    token = RequestEnvelope_pb2.RequestEnvelope.AuthInfo.JWT(
                        contents = self.access_token,
                        unknown2 = 59
                        )
                    )
        # TODO -> This parts need new method to fix multiple authentication
        req = RequestEnvelope_pb2.RequestEnvelope(
                status_code = 2,
                request_id = api.get_RPC_ID(),
                longitude = self.location.lon,
                latitude = self.location.lat,
                altitude = self.location.alt,
                auth_ticket = self.authTicket,
                unknown12 = 989,
                auth_info = info
                )

        data = [None, ] * 4
        data[0] = Request_pb2.Request(
                request_type = RequestType_pb2.GET_HATCHED_EGGS
                )
        data[1] = Request_pb2.Request(
                request_type = RequestType_pb2.GET_INVENTORY,
                request_message = GetInventoryMessage_pb2.GetInventoryMessage(
                    last_timestamp_ms = 0
                    ).SerializeToString()
                )
        data[2] = Request_pb2.Request(
                request_type = RequestType_pb2.CHECK_AWARDED_BADGES
                )
        data[3] = Request_pb2.Request(
                request_type = RequestType_pb2.DOWNLOAD_SETTINGS,
                request_message = DownloadSettingsMessage_pb2.DownloadSettingsMessage(
                    hash="4a2e9bc330dae60e7b74fc85b98868ab4700802d"     # This should be e instead of d.
                    ).SerializeToString()
                )
        payload += data
        req.requests.extend(payload)
        return req

    def request(self, req, url=None):
        try:
            if url is None:
                url = self.endpoint
            # Send request
            rawResponse = self.session.post(url, data=req.SerializeToString())

            res = ResponseEnvelope_pb2.ResponseEnvelope()
            res.ParseFromString(rawResponse.content)

            if res.auth_ticket.start:
                self.authTicket = res.auth_ticket
            return res
        except:
            sys.exit("Can't acquire request from server, Error 64114")
            return 1

    def wrap_and_request(self, payload):
        while True:
            try:
                res = self.request(self.wrap_in_request(payload))
                if res is not None:
                    print(res)
                    # self.parse_default(res)
                    #self.state.eggs.ParseFromString(res.returns[1])
                    #self.state.inventory.ParseFromString(res.returns[2])
                    #self.state.badges.ParseFromString(res.returns[3])
                    #self.state.settings.ParseFromString(res.returns[4])
                    return res
                else:
                    sys.exit("Error to get response from server, Error 12552")
            except:
                print("Sleep ... 1...s")
                time.sleep(1)
                continue
        return res

    def parse_default(self, res):
        #try:
            self.state.eggs.ParseFromString(res.returns[1])
            self.state.inventory.ParseFromString(res.returns[2])
            self.state.badges.ParseFromString(res.returns[3])
            self.state.settings.ParseFromString(res.returns[4])
        #except:
            #sys.exit("Error parsing response. Malformed response, Error 84923")
        
        #item = self.state.inventory.inventory_delta.inventory_items

    def get_map_objects(self):
        payload = self.location.get_objects_message()
        
        res = self.wrap_and_request(payload)
        self.state.mapObjects.ParseFromString(res.returns[0])
        print(self.state.mapObjects)

        for cell in self.state.mapObjects.map_cells:
            print(cell.wild_pokemons)


