# Generated by Django 2.0.6 on 2018-07-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_checkpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('paradigm', models.CharField(max_length=50)),
            ],
        ),
    ]
