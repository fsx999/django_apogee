.. _initialisation:

=========================
Initialisation de la base
=========================

Problèmatique
-------------

Il est nécessaire de faire une copie des donées d'apogée.

Il y a plusieurs stratégies de copie et de synchronisation, la meilleurs étant d'implémenter ça du coté d'oracle.

Mais ici nous partons du principe que ce n'est pas possible et donc nous devons faire une copie de certaines données et une modification pour d'autres.

Une copie mais pour quoi faire ?

Premièrement les clés composites. Il faut copier les données et rajoutés un id qui est la concaténation des clés primaires.

Deuxièmement les données d'apogée sont instables, trop de règles effacent des données nécessaire au fonctionnement d'autres applications de la suite.


Initialisation
--------------

.. warning:: C'est une opération longue, environ 30 minutes

 .. code-block:: bash

   ./manage.py initialisation_base

