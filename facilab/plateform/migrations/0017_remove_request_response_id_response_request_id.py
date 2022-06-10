# Generated by Django 4.0.5 on 2022-06-10 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0016_alter_request_request_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='response_id',
        ),
        migrations.AddField(
            model_name='response',
            name='request_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateform.request'),
        ),
    ]