# Generated by Django 3.1.5 on 2021-04-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
