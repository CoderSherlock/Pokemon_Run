import random
import service


RPC_ID = int(random.random() * 10 ** 13)

def get_RPC_ID():
    global RPC_ID
    RPC_ID =RPC_ID +1
    return RPC_ID


