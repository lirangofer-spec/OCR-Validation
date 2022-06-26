import datetime
import pymongo
from db.connectionString import credentials
import logging
logging.basicConfig(filename='../db.log', format='%(asctime)s - %(message)s', level=logging.DEBUG)


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Methods:
    def __init__(self):
        global myclient
        try:
            myclient = pymongo.MongoClient(
                "mongodb+srv://" + credentials + ".ziihc.mongodb.net/?retryWrites=true&w=majority")
            logging.info('Connected successfully to MongoDB')
        except:
            logging.error('Could not connect to MongoDB')
        mydb = myclient["ocr"]
        self.mycol = mydb["allow"]

    def add(self, platenumber: str, isallowed: bool, filename: str ):
        dict = { "platenumber": platenumber, "isallowed": isallowed, "filename": filename , "timestamp": datetime.datetime.now() }
        self.mycol.insert_one(dict)
        logging.info('Successfully added' + filename + "to DB")

    def get(self, filename: str):
        myquery = {"filename": filename}
        logging.info('Successfully get' + filename + "from DB")
        return self.mycol.find_one(myquery)
