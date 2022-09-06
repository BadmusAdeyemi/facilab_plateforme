# Generated by Django 4.0.5 on 2022-09-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0008_request_categorie_request_contrainte_request_matiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='categorie',
            field=models.CharField(choices=[('Aides techniques', 'Aides techniques'), ('Aides technologiques', 'Aides technologiques'), ('Aides domotiques', 'Aides domotiques'), ('Gabarits', 'Gabarits')], max_length=55, verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='request',
            name='contrainte',
            field=models.CharField(choices=[('Pas de contrainte identifiée', 'Pas de contrainte identifiée'), ('Normes alimentaires', 'Normes alimentaires')], max_length=55, verbose_name='Contrainte'),
        ),
        migrations.AlterField(
            model_name='request',
            name='matiere',
            field=models.CharField(choices=[('Pas de matière prédéfinie', 'Pas de matière prédéfinie'), ('Textile', 'Textile'), ('Métal', 'Métal'), ('Plastique', 'Plastique'), ('Bois', 'Bois')], max_length=55, verbose_name='Matière'),
        ),
    ]