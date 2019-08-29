import os

# Flask settings
FLASK_SERVER_NAME = 'localhost:5000'
# Do not use debug mode in production
FLASK_DEBUG = os.environ.get('FLASK_DEBUG') if os.environ.get('FLASK_DEBUG') is not None else False

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
