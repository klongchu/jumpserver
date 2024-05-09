# Generated by Django 4.1.10 on 2023-09-14 07:23

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0043_remove_user_secret_key_preference'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField(verbose_name='Login IP')),
                ('key', models.CharField(max_length=128, verbose_name='Session key')),
                ('city', models.CharField(blank=True, max_length=254, null=True, verbose_name='Login city')),
                ('user_agent', models.CharField(blank=True, max_length=254, null=True, verbose_name='User agent')),
                ('type', models.CharField(choices=[('W', 'Web'), ('T', 'Terminal'), ('U', 'Unknown')], max_length=2,
                                          verbose_name='Login type')),
                ('backend', models.CharField(default='', max_length=32, verbose_name='Auth backend')),
                ('date_created', models.DateTimeField(blank=True, null=True, verbose_name='Date created')),
                ('date_expired',
                 models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Date expired')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions',
                                           to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User session',
                'ordering': ['-date_created'],
                'permissions': [('offline_usersession', 'Offline user session')],
            },
        ),
    ]
