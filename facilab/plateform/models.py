import uuid
from django.db import models
from django.utils import timezone
from authentication.models import User


class Test(models.Model):
    name = models.fields.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    second_updated = models.DateTimeField(auto_now=True)


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    request_title = models.CharField(max_length=255, verbose_name='Titre')
    request_detail = models.TextField(verbose_name='Description')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    """prescriber_id = models.ForeignKey(Prescriber, blank=True, null=True, on_delete=models.SET_NULL)"""

    def __str__(self):
        return f"{self.request_title} ({self.id})"


"""class Response(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    first_name_leader_project = models.CharField(max_length=125)
    last_name_leader_project = models.CharField(max_length=125)
    phone_leader_project = models.CharField(max_length=10)
    mail_leader_project = models.EmailField()
    comment = models.TextField()
    fablab_id = models.ForeignKey(Fablab, null=True, on_delete=models.SET_NULL)
    request_id = models.ForeignKey(Request, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name_leader_project} {self.last_name_leader_project} of {self.fablab_id}"
"""
