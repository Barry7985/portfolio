# Generated by Django 5.1.3 on 2024-12-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse email')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Numéro de téléphone')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255, verbose_name='Établissement')),
                ('degree', models.CharField(max_length=255, verbose_name='Diplôme')),
                ('field_of_study', models.CharField(max_length=255, verbose_name="Domaine d'études")),
                ('start_date', models.DateField(verbose_name='Date de début')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date de fin')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titre du poste')),
                ('company', models.CharField(max_length=255, verbose_name='Entreprise')),
                ('description', models.TextField(verbose_name='Description du poste')),
                ('start_date', models.DateField(verbose_name='Date de début')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date de fin')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom de la compétence')),
                ('proficiency', models.IntegerField(help_text='Niveau de 1 à 100', verbose_name='Niveau de maîtrise')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titre du projet')),
                ('description', models.TextField(verbose_name='Description du projet')),
                ('start_date', models.DateField(verbose_name='Date de début du projet')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date de fin du projet')),
                ('project_url', models.URLField(blank=True, null=True, verbose_name='URL du projet')),
                ('technologies', models.ManyToManyField(to='myportfolio.skill', verbose_name='Technologies utilisées')),
            ],
        ),
    ]
