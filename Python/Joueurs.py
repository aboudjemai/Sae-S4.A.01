#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:18:56 2024

@author: aboudjemai
"""

from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from Client2Mongo import Client2Mongo

joueurs_bp = Blueprint('joueurs', __name__)

bd = Client2Mongo("iut_boudjemai")
    
    
@joueurs_bp.route('/joueurs/nbJoueurs', methods=['GET'])
def nombre_de_joueur():
    nb_joueurs = bd.bd["joueurs"].count_documents({})
    return jsonify(nb_joueurs)
       
    
@joueurs_bp.route('/joueurs', methods=['POST'])
def inserer_joueur():
    joueur = request.json
    collJoueur = bd.get_collection("joueurs")
    insertion = collJoueur.insert_one(joueur)
    return jsonify({"id": str(insertion.inserted_id)})


@joueurs_bp.route('/joueurs/<string:nom>', methods=['GET'])
def chercher_joueur(nom):
    collection = bd.get_collection("joueurs")
    joueur = collection.find_one({"nom": nom})
    
    if joueur is None:
        return ("erreur")
    else:
        return jsonify(joueur)
