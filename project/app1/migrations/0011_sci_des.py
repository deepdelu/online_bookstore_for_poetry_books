# Generated by Django 4.2 on 2023-05-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_sci'),
    ]

    operations = [
        migrations.AddField(
            model_name='sci',
            name='des',
            field=models.TextField(default='Description'),
        ),
    ]
