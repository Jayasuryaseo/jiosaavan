# Generated by Django 4.2.1 on 2023-06-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiosaavan', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Password',
            field=models.CharField(default='', max_length=20),
        ),
    ]
