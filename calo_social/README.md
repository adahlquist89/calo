calo-social
====================

usa el pinax-social-project

Como usarlo:
=============
	//crear un env para instalar las cosas:
    $ virtualenv socialenv
    //activarlo:
    $ source mysite/bin/activate
    (socialenv)$ cd calo-social
    //instalar los requerimientos (instala apps necesarias y Django)
    (socialenv)$ pip install -r requirements.txt
    (socialenv)$ python manage.py syncdb
    (socialenv)$ python manage.py runserver

ir a http://127.0.0.1:8000 para ver el sitio


