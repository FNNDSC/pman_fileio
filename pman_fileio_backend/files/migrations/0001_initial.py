# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.FileField(max_length=200, upload_to='')),
            ],
        ),
    ]