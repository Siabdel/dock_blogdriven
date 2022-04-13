# Generated by Django 2.2.13 on 2020-11-24 11:51

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'signature',
                'verbose_name_plural': 'signatures',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_email', models.BooleanField(default=True, verbose_name='send email')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notifications.Signature')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='followers')),
                ('linked_streams', models.ManyToManyField(blank=True, to='notifications.Stream', verbose_name='linked streams')),
            ],
            options={
                'verbose_name': 'stream',
                'verbose_name_plural': 'streams',
            },
        ),
        migrations.AddField(
            model_name='signature',
            name='subscribers',
            field=models.ManyToManyField(blank=True, through='notifications.Subscription', to=settings.AUTH_USER_MODEL, verbose_name='subscribers'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('read', models.DateTimeField(blank=True, null=True, verbose_name='read on')),
                ('dispatch_uid', models.CharField(max_length=32, verbose_name='dispatch UID')),
                ('signature', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notifications.Signature', verbose_name='signature')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
                'ordering': ('-created', 'id'),
                'get_latest_by': '-created',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('signature', models.CharField(max_length=50, verbose_name='signature')),
                ('template', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='template')),
                ('context', models.TextField(blank=True, help_text='Use the JSON syntax.', null=True, validators=[core.models.validate_json], verbose_name='context')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('backlink', models.CharField(blank=True, max_length=200, null=True, verbose_name='backlink')),
                ('streams', models.ManyToManyField(to='notifications.Stream', verbose_name='streams')),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
                'ordering': ('-created',),
            },
        ),
    ]