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

SUPERSET_APP_ROOT = '/superset'
APPLICATION_ROOT = '/superset'
STATIC_ASSETS_PREFIX = '/superset'
