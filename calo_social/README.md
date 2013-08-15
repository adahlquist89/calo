calo-social
====================

usa el pinax-social-project

Como usarlo:
=============
	//crear un env para instalar las cosas:
    $ virtualenv socialenv
    //activarlo:
    $ source mysite/bin/activate
    //creo el proyecto
    (socialenv)$ django-admin startproject --template=calo_social social
    (socialenv)$ cd social
    //instalar los requerimientos (instala apps necesarias y Django)
    (socialenv)$ pip install -r requirements.txt
    (socialenv)$ python manage.py syncdb
    (socialenv)$ python manage.py runserver

ir a http://127.0.0.1:8000 para ver el sitio

IMPORTANTE:
============
la autentificación con Google, facebook, etc, no va a andar si lo corremos desde localhost. Hay que correrle en un servidor o algo. 
Investigar Google AppEngine para hacer las pruebas.


