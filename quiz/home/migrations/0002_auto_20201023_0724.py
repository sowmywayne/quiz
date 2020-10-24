# Generated by Django 3.1.2 on 2020-10-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rm', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='rmdID',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]