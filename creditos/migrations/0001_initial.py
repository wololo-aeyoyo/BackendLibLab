# Generated by Django 3.2.4 on 2021-06-27 20:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='puntuacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='creditos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deuda', models.FloatField()),
                ('AlgoritoIa', models.FloatField()),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('id_puntuacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditos.puntuacion')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creditos.usuarios')),
            ],
        ),
    ]
