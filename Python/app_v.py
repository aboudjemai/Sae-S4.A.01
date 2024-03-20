#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:15:44 2024

@author: aboudjemai
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:30:27 2024

@author: aboudjemai
"""

from flask import Flask
from flask_cors import CORS
from Joueurs import joueurs_bp
from Tournoi import tournoi_bp

app = Flask(__name__)
CORS(app)  

app.register_blueprint(joueurs_bp, url_prefixes='/joueurs')
app.register_blueprint(tournoi_bp, url_prefixes='/tournoi')

if __name__ == '__main__':
    app.run(debug=True)


