# Generated by Django 4.0.5 on 2022-06-10 14:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plateform', '0014_rename_answer_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_title', models.CharField(max_length=255)),
                ('request_detail', models.CharField(max_length=1000)),
                ('applicant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateform.applicant')),
                ('prescriber_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateform.prescriber')),
                ('response_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='plateform.response')),
            ],
        ),
    ]
