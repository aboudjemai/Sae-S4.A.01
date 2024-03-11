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
from collection_routes import collections_bp

app = Flask(__name__)

app.register_blueprint(collections_bp, url_prefixes='/collections')


if __name__ == '__main__':
    app.run(debug=True)