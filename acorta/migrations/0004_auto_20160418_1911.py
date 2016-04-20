# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0003_auto_20160417_1112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='urlCortas',
            new_name='noticias',
        ),
        migrations.DeleteModel(
            name='urlLargas',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='urlLarga',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='urlCorta',
            new_name='titulo',
        ),
    ]
