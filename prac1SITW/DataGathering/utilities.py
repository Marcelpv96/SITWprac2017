from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import requests
import urlparse


def setup_django():
    import os
    import sys
    import django

    sys.path.append("../prac1SITW")
    os.environ["DJANGO_SETTINGS_MODULE"] = "prac1SITW.settings"
    django.setup()


def save_image_from_url(field, url):
    r = requests.get(url)

    if r.status_code == requests.codes.ok:
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(r.content)
        img_temp.flush()

        img_filename = urlparse.urlsplit(url).path[1:]

        field.save(img_filename, File(img_temp), save=True)

        return True

    return False

