#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initialize the MongoClient with your MongoDB connection details
        self.USER = username
        self.PASS = password
        self.HOST = 'nv-desktop-services.apporto.com'
        self.PORT = 30807
        self.DB = 'AAC'
        self.COL = 'animals'
        self.client = MongoClient(f'mongodb://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}')
        self.database = self.client[self.DB]
        self.collection = self.database[self.COL]

    def create(self, data):
        """Inserts a document into the specified MongoDB database and collection.

        Args:
            data (dict): A dictionary representing the key-value pairs for the document.

        Returns:
            bool: True if the insert is successful, else False.
        """
        if data:
            result = self.collection.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, query):
       
        if query:
            cursor = self.collection.find(query)
            return list(cursor)
        
    def read(self, query=None):
        cursor = self.collection.find(query) if query else self.collection.find()
        return list(cursor)
            
    def update(self, query, update_data):
        
        if query and update_data:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        else:
            raise ValueError("Query or update_data parameters are empty")
            
    def delete(self, query):
        
        if query:
            result = self.collection.delete_many(query)
            return result.deleted_count
        else:
            raise ValueError("Query parameter is empty")
                                               

