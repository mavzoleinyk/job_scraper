import codecs
import os, sys

from django.contrib.auth import get_user_model
from django.db import DatabaseError

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scrap_service.settings'

import django
django.setup()

from scraping.parsers import*

from scraping.models import Vacancy, City, Language, Error, Url

User = get_user_model()

parsers = (
    (work, 'work'),
    (rabota, 'rabota'),
    (dou, 'dou'),
    (djinni, 'djinni'),
    (rabotaru, 'rabotaru')
    )

def get_settings():
    qs = User.objects.filter(send_email = True).values()
    settings_list = set((q['city_id'], q['language_id']) for q in qs)
    return settings_list

def get_urls(_settings):
    qs = Url.objects.all().values()
    url_dct = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        tmp = {}
        tmp['city'] = pair[0]
        tmp['language'] = pair[1]
        tmp['url_data'] = url_dct[pair]
        urls.append[tmp]
    return urls

q = get_settings()
u = get_urls(q)

city = City.objects.filter(slug='kiev').first()
language = Language.objects.filter(slug='python').first()

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e
if errors:
    er = Error(data=errors).save()


# h = codecs.open('work.txt', 'w', 'utf-8')
# h.write(str(jobs))
# h.close()