.. Django apogee documentation master file, created by
   sphinx-quickstart on Wed Mar 12 11:27:50 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation de Django apogee
==============================

This is a french application for french university. It's why the documentaion is in French.

Cette application a pour but de fournir les modèles et méthodes d'accès à certaines tables d'Apogée.

Elle fait partie d'une suite d'application Django nommée Duck-Duck mais peut être utilisée seule.


.. note::
   Django ne supporte pas les clés primaires composites.
   C'est pourquoi certaines Modèle possèdent un équivalent NomInitialeCopy qui correspondent à la table initiale + un id.

   L'id correspond à la concaténation des clés primaires.

   Les Modèles initiaux ne doit être utilisés que dans certains cas de lecture (c'est à dire pour la copie des données).

   Voir la documentation des tables concernées




Table des matières:

.. toctree::
   :maxdepth: 3

   installation.rst
   prerequis.rst
   auto_modules.rst





Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

