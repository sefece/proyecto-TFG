# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('applicant', models.ForeignKey(to='backend.Applicant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('bidder', models.ForeignKey(to='backend.Bidder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Revisor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tag_name', models.CharField(max_length=200)),
                ('tag_description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='revisor',
            name='user',
            field=models.ForeignKey(to='backend.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='offer',
            name='revisor',
            field=models.ManyToManyField(to='backend.Revisor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.ForeignKey(to='backend.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bidder',
            name='user',
            field=models.ForeignKey(to='backend.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='offer',
            field=models.ForeignKey(to='backend.Offer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='user',
            field=models.ForeignKey(to='backend.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.ForeignKey(to='backend.User'),
            preserve_default=True,
        ),
    ]
