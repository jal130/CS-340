from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:42109'%(user,password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, animal_data):
        if animal_data is not None:
            print("----------------------- Inserting New Animal ------------------")
            self.database.animals.insert_one(animal_data)  # data should be dictionary
            print("-------------- Done -------------------------------------------")
        else:
            raise Exception("Failed to add Data")
            
    #Create method to implement the R in CRUD.
    def read(self, criteria):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id":False})  # data should be dictionary 
            return data
        else:
            raise Exception("nothing to read, hint is empty")
            
            
    # this method is used to delete animal from the db
    def delete(self, _animal):
        if _animal is not None:
            data = self.read(_animal) # find animal first
            if data is None:
                print("Animal does not eists")
                return
            self.database.animals.delete_many(_animal)  # data should be dictionary 
        else:
            raise Exception("nothing to delete, animal data is empty")
            
    # used for updating animal
    def update(self, _criteria,_newData):
        if _criteria is not None and _newData is not None:
            self.database.animals.updateOne(_criteria,{'$set':_newData}) 
            self.read(_newData)
            
        else:
            raise Exception("please enter both key and data to modify the collection")