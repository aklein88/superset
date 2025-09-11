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

SUPERSET_APP_ROOT = '/analytics'
APPLICATION_ROOT = '/analytics'
STATIC_ASSETS_PREFIX = '/analytics'

# Translations
BABEL_DEFAULT_LOCALE = 'fr'
BABEL_DEFAULT_FOLDER = 'superset/translations'
LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    'fr': {'flag': 'fr', 'name': 'Français'},
}