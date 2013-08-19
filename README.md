calo
====

Ideas y apps para usar:
=======================

Creo que lo mejor es partir del pinax-social-project que ya viene con el manejo de cuentas incorporado y a partir de ahí sacar/agregar apps. Por ejemplo, la app "friends" creo que está medio obsoleta pero podemos usar una que es django-friendship o kaleo.

Para la creación de cuentas se usa el OAuth y el django-users-accounts. 

Yo estoy retocando el proyecto pinax-social, porque sólo permitía el sign up de usuarios con las redes sociales pero no usaba el user-accounts. Hay que retocar un poco los templates y listo. 

Eso es todo por ahora.

Ideas para que el trabajo sea ordenado.
=======================================

1) Usar doc strings de python en toda función.
Pueden ser accedidas en runtime 
 foo.__doc__

o usando help(foo)