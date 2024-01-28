#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.pu createsu
if [[ $CREATE_SUPERUSER ]]; then
  python world_champ_2022/manage.py createsuperuser --no-input
fi
