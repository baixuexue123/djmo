# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('privilege', models.IntegerField(default=1, verbose_name='\u6743\u9650', choices=[(1, '\u666e\u901a'), (2, '\u4e2d\u7ea7'), (3, '\u9ad8\u7ea7'), (4, '\u8d85\u7ea7')])),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u9644\u52a0\u4fe1\u606f',
                'verbose_name_plural': '\u9644\u52a0\u4fe1\u606f\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u89d2\u8272',
                'verbose_name_plural': '\u89d2\u8272\u5217\u8868',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(verbose_name='\u89d2\u8272', to='accounts.Role'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
