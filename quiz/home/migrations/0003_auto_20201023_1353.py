# Generated by Django 3.1.2 on 2020-10-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201023_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='rmdID',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='rm',
            field=models.CharField(max_length=200),
        ),
    ]