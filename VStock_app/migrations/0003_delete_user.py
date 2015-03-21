# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VStock_app', '0002_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]
