# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VStock_app', '0003_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Balance',
            new_name='balance',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='stocks_owned',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
