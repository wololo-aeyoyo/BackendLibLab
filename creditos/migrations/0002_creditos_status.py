# Generated by Django 3.2.4 on 2021-06-27 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creditos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditos',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
