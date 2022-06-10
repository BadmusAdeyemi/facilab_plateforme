# Generated by Django 4.0.5 on 2022-06-10 12:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0012_alter_fablab_mail_fablab_alter_fablab_phone_fablab_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fablab',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prescriber',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name_leader_project', models.CharField(max_length=125)),
                ('last_name_leader_project', models.CharField(max_length=125)),
                ('phone_leader_project', models.CharField(max_length=10)),
                ('mail_leader_project', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('fablab_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateform.fablab')),
            ],
        ),
    ]
