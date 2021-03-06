# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-08 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='comment',
            new_name='quote',
        ),
        migrations.AddField(
            model_name='favorite',
            name='User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Favorite', to='quotes_app.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quote',
            name='favorites',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav', to='quotes_app.Favorite'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='postedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to='quotes_app.User'),
        ),
    ]
