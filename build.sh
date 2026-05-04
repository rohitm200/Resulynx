#!/usr/bin/env bash

set -e

pip install -r requirements.txt

# Run database migrations before collecting static files
python manage.py migrate

python manage.py collectstatic --noinput
