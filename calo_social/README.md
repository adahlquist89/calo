calo-social
====================

usa el pinax-social-project

Como usarlo:
=============
	//entrar a directorio del repo
	//crear un env para instalar las cosas:
    dir_repo$ virtualenv socialenv
    //activarlo:
    dir_repo$ source socialenv/bin/activate
    (socialenv)$ cd calo_social
    //instalar los requerimientos (instala apps necesarias y Django)
    (socialenv)dir_repo/calo_social$ pip install -r requirements.txt
    (socialenv)dir_repo/calo_social$ python manage.py syncdb
    (socialenv)dir_repo/calo_social$ python manage.py runserver

ir a http://127.0.0.1:8000 para ver el sitio

IMPORTANTE:
============
la autentificación con Google, facebook, etc, no va a andar si lo corremos desde localhost. Hay que correrle en un servidor o algo. 
Investigar Google AppEngine para hacer las pruebas.


