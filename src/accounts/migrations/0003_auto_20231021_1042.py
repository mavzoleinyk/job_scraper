# Generated by Django 3.2.4 on 2023-10-21 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0004_url'),
        ('accounts', '0002_auto_20231021_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scraping.language'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scraping.city'),
        ),
    ]
