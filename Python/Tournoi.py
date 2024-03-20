#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:18:56 2024

@author: aboudjemai
"""

from flask import Blueprint, jsonify, request
from Client2Mongo import Client2Mongo
from bson.objectid import ObjectId
import re

class Tournoi:
    def __init__(self, nom: str, date: str, format: str, categorie):
        if not isinstance(nom, str):
            raise ValueError("Le nom du tournoi doit être une chaîne de caractères")
        if not re.match(r"\d{2}/\d{2}/\d{4}", date):
            raise ValueError("La date doit être au format jj/mm/aaaa")
        self.nom = nom
        self.date = date
        self.format = format
        self.categorie = categorie
        
    def modifier_tournoi(self, nom: str = None, date: str = None, format: str = None, categorie = None):
        if nom is not None:
            self.nom = nom
        if date is not None:
            self.date = date
        if format is not None:
            self.format = format
        if categorie is not None:
            self.categorie = categorie

        print(f"Tournoi modifié : {self.nom}, Date : {self.date}, Format : {self.format}, Catégorie : {self.categorie}")

    
    
    

tournoi_bp = Blueprint('tournoi', __name__)

bd = Client2Mongo("iut_boudjemai")
    
    
@tournoi_bp.route('/tournoi', methods=['GET'])
def liste_tournoi():
    try:
        tournois_resultat = bd.get_collection("tournois").find()
        liste_tournois = [tournoi for tournoi in tournois_resultat]
        for tournoi in liste_tournois:
            tournoi['_id'] = str(tournoi['_id'])
        return jsonify(liste_tournois)
    except Exception as excep:
        return jsonify({"etat": "pas ok"})
    
    

@tournoi_bp.route('/tournoi/modification/<id>', methods=['PATCH'])
def modif_tournoi(id):
    try:
        if request.json:
            formatOk = request.json.get('format')
        else:
            formatOk = request.form.get('format')
            
        if not formatOk:
            return jsonify({"etat": "pas ok"})
        
        bdRep = bd.get_collection("tournois").update_one(
            {"_id": ObjectId(id)},
            {"$set": {"format": formatOk}}
        )
        return jsonify({"etat": "ok"})
    except Exception as excep:
        return jsonify({"etat": "pas ok"})

    
