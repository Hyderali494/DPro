# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-12 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Phone_no', models.IntegerField(default=0)),
            ],
        ),
    ]
