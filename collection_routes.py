#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:18:56 2024

@author: aboudjemai
"""

from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from Client2Mongo import Client2Mongo
import pprint

collections_bp = Blueprint('collections', __name__)

bd = Client2Mongo("iut_boudjemai")
    
    
@collections_bp.route('/collections', methods=['GET'])
def list_des_coll():
        collections = bd.liste_des_collections()
        return jsonify(collections)
       
    
@collections_bp.route('/collections', methods=['POST'])
def inserer_joueur():
    joueur = request.json
    collJoueur = bd.get_collection("joueurs")
    insertion = collJoueur.insert_one(joueur)
    return jsonify({"id": str(insertion.inserted_id)})
