web: gunicorn  Dinamo Dinamo.wsgi --log-file - --log-level debug
web: python project-Dinamo/manage.py runserver 0.0.0.0:$PORT
python manage.py collectstatic --noinput
python manage.py migrate
