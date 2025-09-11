#!/bin/bash

# Configure translation
# https://github.com/apache/superset/discussions/31444

pybabel init -i superset/translations/messages.pot -d superset/translations -l fr

./scripts/translations/babel_update.sh
pybabel update -i superset/translations/messages.pot -d superset/translations --ignore-obsolete

cd superset-frontend
npm ci
npm run build-translation