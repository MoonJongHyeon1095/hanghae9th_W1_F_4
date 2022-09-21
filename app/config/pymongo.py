from pymongo import MongoClient
import certifi

ca = certifi.where()

class Pymongo:
    client = MongoClient("mongodb+srv://test:sparta@cluster0.g2d328l.mongodb.net/?retryWrites=true&w=majority",
                         tlsCAFile=ca, tls=True, tlsAllowInvalidCertificates=True)
    db = client.minibook