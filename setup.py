from distutils.core import setup

setup(name='django_apogee', version='0.0.1',
      packages=['', 'django_apogee', 'django_apogee.models', 'django_apogee.management',
                'django_apogee.management.commands'], url='https://github.com/fsx999/django_apogee', license='bsd 3',
      author='paul guichon', author_email='paul.guichon@iedparis8.net', description='',
      install_requires=['django',
                        'south',
                        ])
