# coding=utf-8
# coding=utf-8
from django.apps import AppConfig


class DuckApogee(AppConfig):
    name = "django_apogee"
    label = 'django_apogee'

    collapse_settings = [
    {
        "group_label": "Django_Apogee",
        "icon": 'fa-fw fa fa-circle-o',
        "entries": [{
            "label": 'Settings année universitaire',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/django_apogee/confanneeuni/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }, ]