# Generated by Django 5.1.6 on 2025-02-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='marks',
            field=models.FloatField(default=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='roll',
            field=models.IntegerField(default=101),
            preserve_default=False,
        ),
    ]
