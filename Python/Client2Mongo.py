#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:41:09 2024

@author: aboudjemai
"""

from pymongo import MongoClient


class Client2Mongo:
    def __init__(self, iut_boudjemai, uri="mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.bd = self.client[iut_boudjemai]
        
    def liste_des_collections(self):
        return self.bd.list_collection_names()
    
    def get_collection(self, coll):
        return self.bd[coll]
    
    def find_one(self, collection_name):
        return self.bd[collection_name].find_one()
    
    def find(self, collection_name):
        return self.bd[collection_name].find()
    

    
    