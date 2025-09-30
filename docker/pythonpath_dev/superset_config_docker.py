#FEATURE_FLAGS = {
#    'ENABLE_TEMPLATE_PROCESSING': True,
#    'ESCAPE_MARKDOWN_HTML': False
#}

HTML_SANITIZATION = True
HTML_SANITIZATION_SCHEMA_EXTENSIONS = {
  "attributes": {
    "*": ["style", "className", "class"],
  },
  "tagNames": ["style"],
}

GLOBAL_ASYNC_QUERIES = True
GLOBAL_ASYNC_QUERIES_TRANSPORT = "ws"
GLOBAL_ASYNC_QUERIES_WEBSOCKET_URL = "ws://my.domain.com/ws:8080/" # use wss protocol (wss:) for SSL connection
GLOBAL_ASYNC_QUERIES_JWT_SECRET = "YOUR_CUSTOM_JWT_SECRET"
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_NAME = "async-token"

TALISMAN_CONFIG = {
    "content_security_policy": {
        "connect-src": [
            "'self'",
            "ws://my.domain.com/ws",  # Add your websocket endpoint here, use wss protocol (wss:) for SSL connection
        ],
    },
}

# Translations
BABEL_DEFAULT_LOCALE = 'fr'
BABEL_DEFAULT_FOLDER = 'superset/translations'
LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    'fr': {'flag': 'fr', 'name': 'Français'},
}