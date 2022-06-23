web: gunicorn --pythonpath Dinamo Dinamo.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate