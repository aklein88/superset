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
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_NAME = "async-token"
#GLOBAL_ASYNC_QUERIES_JWT_SECRET = "YOUR_CUSTOM_JWT_SECRET"
#GLOBAL_ASYNC_QUERIES_WEBSOCKET_URL = "ws://my.domain.com/ws" # use wss protocol (wss:) for SSL connection

TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "default-src": ["'self'"],
        "script-src": ["'self'", "https://trusted-scripts.com"],
        "img-src": ["'self'", "data:"],
        "connect-src": [
            "'self'",
            "ws://my.domain.com/ws",  # Add your websocket endpoint here, use wss protocol (wss:) for SSL connection
            "https://api.mapbox.com"
        ],
    },
}
