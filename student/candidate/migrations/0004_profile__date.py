# Generated by Django 5.1.6 on 2025-02-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0003_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='_date',
            field=models.DateTimeField(null=True),
        ),
    ]
