# Generated by Django 3.2.4 on 2023-06-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_remove_sci_des_alter_base_id_alter_cont_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='description',
            field=models.CharField(default='Description', max_length=500),
        ),
    ]
