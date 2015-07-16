# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('sec', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='heart',
            name='video',
            field=models.ForeignKey(to='api.Video'),
        ),
    ]
