# Generated by Django 2.0 on 2021-08-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='photo',
            field=models.ImageField(default='', upload_to='img/'),
        ),
    ]
