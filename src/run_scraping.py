import codecs
import os, sys

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'scrap_service.settings'

import django
django.setup()

from scraping.parsers import*

from scraping.models import Vacancy, City, Language, Error


parsers = (
    (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
    (rabota, 'https://robota.ua/zapros/python/kyiv'),
    (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D1%97%D0%B2&category=Python'),
    (djinni, 'https://djinni.co/jobs/?primary_keyword=Python&region=UKR&location=kyiv'),
    (rabotaru, 'https://rostov.rabota.ru/vacancy/?query=python&location.ll=47.222078,39.720358&location.kind=region&location.radius=any&location.regionId=284&location.name=%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2-%D0%BD%D0%B0-%D0%94%D0%BE%D0%BD%D1%83&sort=distance')
    )
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