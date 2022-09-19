from pymongo import MongoClient

class Pymongo:
    client = MongoClient("mongodb+srv://test:sparta@cluster0.g2d328l.mongodb.net/?retryWrites=true&w=majority", 
        tls=True, tlsAllowInvalidCertificates=True)
    db = client.minibook