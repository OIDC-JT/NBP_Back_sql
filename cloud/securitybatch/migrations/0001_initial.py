# Generated by Django 3.2.15 on 2022-08-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Securitybatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servertype', models.TextField(max_length=100)),
                ('servername', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Securitybatchsub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('servertype', models.TextField(max_length=100)),
                ('servername', models.TextField(max_length=100)),
            ],
        ),
    ]
