# Generated by Django 2.2.10 on 2021-05-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fluxo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entradas', models.IntegerField()),
                ('saidas', models.IntegerField()),
            ],
        ),
    ]
