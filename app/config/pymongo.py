from pymongo import MongoClient
from .env import *
import certifi

ca = certifi.where()

class Pymongo:
    client = MongoClient(URL,
                         tlsCAFile=ca, tls=True, tlsAllowInvalidCertificates=True)
    db = client.minibook