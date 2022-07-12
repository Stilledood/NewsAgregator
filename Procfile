web: gunicorn  Dinamo Dinamo.wsgi --log-file - --log-level debug
web: Dinamo/python manage.py runserver 0.0.0.0:$PORT
web: Dinamo/python manage.py collectstatic --noinput
web: Dinamo/python manage.py migrate
web : Dinamo/python manage.py startjobs
