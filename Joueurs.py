#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:41:09 2024

@author: aboudjemai
"""
from Client2Mongo import Client2Mongo
from pymongo import MongoClient
import pprint

class Joueurs:
    def __init__(self):
        self.connectionBd = Client2Mongo("iut_boudjemai")
        
    def liste_joueurs(self):
        return self.connectionBd.get_collection("joueurs").find()

if __name__ == "__main__":
    
    j = Joueurs()
    
    for joueurs in j.liste_joueurs():
        pprint.pprint(joueurs)
        print(" ")
