============
Installation
============

L'installation décrite ci-dessous vaut pour une ubuntu server 13.10.
Dans le cas d'un autre système d'exploitation veuillez adapter les commandes ci-dessous.

Prérequis
---------

Il faut avoir un accès en lecture pour apogée pour la liste des tables suivantes : .....

Et un accès en écriture sur les tables OPI.

Toutes les commandes ci-dessous se font en tant qu'utilisateur normale. Il faut donc tenir compte des sudo pour les
commandes en temsp que superutilisateur, et sans le sudo pour les commandes en tant qu'utilisateur normal.

.. warning::
  L'installation du virtualenv ne doit pas se faire en tant que root pour des raisons de sécurité.
  De plus pour tous les paquets pythons, il faut passer par le gestionnaire pip et non par le gestionnaire de paquet du
  système.


Commandes
---------


#) Installation de pip :
    .. code-block:: bash

      sudo apt-get install python-setuptools
      sudo easy_install pip


#) Installation de virtualenv

    .. code-block:: bash

      sudo pip install virtualenv


#) Création du virtualenv

    .. code-block:: bash

      mkdir .Envs
      cd .Envs
      virtualenv django_projet

    Pour rappel : VirtualEnv permet de faire une genre de sandbox pour les applications pythons. Pour activer le virtualenv

    .. code-block:: bash

      source ~/.Envs/django_projet/bin/activate


#) Installation de postgresql

    .. code-block:: bash

      sudo apt-get install postgresql libpq-dev

    Configuration de postgresql

    .. code-block:: bash

      sudo -i -u postgres
      createuser -P mon_utilisateur
      createdb -O mon_utilisateur -E UTF8 ma_database

    mon_utilisateur et ma_database serviront pour la connection à la base postgresql




