#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:54:32 2024

@author: aboudjemai
"""

import unittest
from Tournoi import Tournoi

# Assuming Tournoi class definition is as provided above

class TestTournoi(unittest.TestCase):
    def test_nom_tournoi_uniquement_chaineCarac(self):
        with self.assertRaises(ValueError):
            Tournoi(nom=867987, date="2024-03-18", format="Simple", categorie="Amateur")
            
    def test_format_date(self):
            with self.assertRaises(ValueError):
                Tournoi(nom="test", date="2024-03-18", format="Simple", categorie="Amateur")

if __name__ == '__main__':
    unittest.main()

