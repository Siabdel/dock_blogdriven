# Generated by Django 2.2 on 2021-04-21 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('recap', models.CharField(default='', max_length=500)),
                ('content', mdeditor.fields.MDTextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified on')),
                ('active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mes_article', to='taxonomy.Category', verbose_name='categories')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ('created', 'title'),
            },
        ),
    ]
