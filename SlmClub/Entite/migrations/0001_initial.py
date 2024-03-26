# Generated by Django 5.0.2 on 2024-02-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_commune', models.CharField(max_length=100)),
                ('description_commune', models.TextField()),
                ('nom_maire', models.CharField(max_length=100)),
                ('etoile_commune', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Quittance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_quittance', models.CharField(max_length=100)),
                ('libelle_quittance', models.TextField()),
                ('date_quittance', models.DateField()),
            ],
        ),
    ]