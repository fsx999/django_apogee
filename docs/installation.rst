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

    installation du connecteur python

    .. code-block:: bash

      source ~/.Envs/django_projet/bin/activate
      pip install psycopg2


#) Installation d'instant client d'oracle:
    Télécharger sur http://www.oracle.com/technetwork/database/features/instant-client/index-097480.html
    la version 11.2 de instant client (nécessite la création d'un compte)
    Deux zip à télécharger : instantclient-basic-linux.ARCH.Version.zip et instantclient-sdk-linux.ARCH.Version.zip
    exemple :

    .. code-block:: bash

      wget http://download.oracle.com/otn/linux/instantclient/11204/instantclient-basic-linux.x64-11.2.0.4.0.zip
      wget http://download.oracle.com/otn/linux/instantclient/11204/instantclient-sdk-linux.x64-11.2.0.4.0.zip

    une fois les zips téléchargés :

    .. code-block:: bash

      sudo mv instantclient-basic-linux.x64-11.2.0.4.0.zip /opt
      sudo mv instantclient-sdk-linux.x64-11.2.0.4.0.zip /opt
      sudo apt-get install unzip
      sudo unzip instantclient-basic-linux.x64-11.2.0.4.0.zip
      sudo unzip instantclient-sdk-linux.x64-11.2.0.4.0.zip
      sudo rm instantclient-basic-linux.x64-11.2.0.4.0.zip
      sudo rm instantclient-sdk-linux.x64-11.2.0.4.0.zip
      cd instantclient_11_2/
      sudo ln -s libclntsh.so.11.1 libclntsh.so
      sudo ln -s libocci.so.11.1 libocci.so

    ensuite rajouté dans le .bashrc de son user

    .. code-block:: bash

      export ORACLE_HOME=/opt/instantclient_11_2
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME
      source ~/.bashrc

#) installation de cx_oracle

    .. code-block:: bash

      sudo apt-get install python-dev
      pip install cx_oracle

#) ajout de django_apogee

    .. code-block:: bash

      sudo apt-get install git
      source ~/.Envs/django_projet/bin/activate
      pip install git+https://github.com/fsx999/django_apogee.git


#) test de l'installation

    .. code-block:: bash

      cd ~
      mkdir projet
      cd projet
      django-admin.py startproject test_projet
      cd test_projet
      chmod +x manage.py

    on peut installer django-extensions et ipython pour améliorer la console de django

    .. code-block:: bash

      pip install django-extensions
      pip install ipython

    configuration du settings.py

    .. code-block:: python

      # après INSTALLED_APPS
      INSTALLED_APPS += (
      'django_extensions',
      'django_apogee',
      'south'
      )

      # La connection aux bases de donnée
      DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'ma_base',
            'USER': 'mon_utilisateur',
            'PASSWORD': 'mon_password!',
            'HOST': '',
            'PORT': '',

        },
        'oracle': {
            'ENGINE': 'django.db.backends.oracle',
            'NAME': 'nom_de_la_base_oracle_apogee',
            'USER': 'utlisateur',
            'PASSWORD': 'password',
            'HOST': 'url_serveur_oracle',
            'PORT': 'port_oracle',
        },
      }

    .. code-block:: bash

      .manage.py syncdb
      .manage.py migrate
      ./manage.py test_connection_apogee

    si le test de connection fonctionne, passez à la suite : :ref:`initialisation`



