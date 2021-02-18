from app import create_app
from app.controllers.server import serverController

from flask import redirect

import logging

app = create_app()

# Get flask logger
logger = logging.getLogger('flask.app')

# create a handler
ch = logging.StreamHandler()

# create formatter
formatter = logging.Formatter('%(levelname)s - %(message)s')

ch.setFormatter(formatter)
ch.setLevel(logging.INFO)

# add handler and level to flask logger
logger.addHandler(ch)
logger.setLevel(logging.INFO)


if __name__ == '__main__':  # only in dev
    app.run(host='0.0.0.0', port=8080, debug=True)