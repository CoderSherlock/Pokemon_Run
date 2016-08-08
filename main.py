#!/usr/bin/python
import os
import time
import re
import sys
import argparse
from gpsoauth import perform_oauth, perform_master_login

import service


# Thanks to Mila432
# TODO -> auth acquire method replacement
AID = '9774d56d682e549c'
SVC= 'audience:server:client_id:848232511240-7so421jotr2609rmqakceuu1luuq0ptb.apps.googleusercontent.com'
APP = 'com.nianticlabs.pokemongo'
CSG = '321187995bc7cdc2b5fc91b11a96e2baa8602c62'


def google_login_auth(usr, passwd):
    try:
        tmp1 = perform_master_login(usr, passwd, AID)
        tmp2 = perform_oauth(usr, tmp1.get('Token', ''), AID, SVC, APP, CSG)
        return tmp2['Auth']
    except:
        print("Can't login to google server, exit code 1")
        sys.exit()


def get_token(usr, passwd):
    token = None
    print('[SH]\tLogin with:\t' + usr)
    token = google_login_auth(usr, passwd)

    return token

def main():
    os.system("clear")

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Login", default=None)
    parser.add_argument("-p", "--password", help="Password", default=None)
    parser.add_argument("-l", "--location", help="Location", required=True)
    parser.add_argument("-m", "--mode", help="Gamemode",default=None)
    global args 
    args = parser.parse_args()
    
    if not args.username:
        args.username = getpass('Username:')
    if not args.password:
        args.password = getpass('Password:')
    access_token = get_token(args.username, args.password)
    # print(access_token)
    if access_token is not None:
        serv = service.Service(access_token, args.location)
    else:
        print("This code should not be ran forever!\n")




if __name__ == '__main__':
    main()

