# Generated by Django 4.0.5 on 2022-06-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0005_applicant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='postcode',
            field=models.IntegerField(null=True),
        ),
    ]