from .serverRoute import bp
from app.routes.swagger import doc_specs


from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = '/docs'
API_URL = '/search/doc_specs'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Challenge Devtools - Backend API"
    }
)

# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = (
    ("/", ),
    ("/alert", ),
    ("/server", ),
    (SWAGGER_URL, swaggerui_blueprint)
)

