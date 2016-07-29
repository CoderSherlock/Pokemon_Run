import argparse
import sys
import location

def restart_process():
    return 1


def start_process(token, location_name=""):
    loca = location.Location()
    loca.set_location_name(location_name);
    print('[SE]\tGoogle token: '+ token[:40])
    

