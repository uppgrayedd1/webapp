from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.CharField(max_length=20, blank=True, null=False)

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('new-activity')


class DailyActivity(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey('mgmt.Properties', null=False, on_delete=models.DO_NOTHING)
    activity = models.ForeignKey(Activities, null=False, on_delete=models.DO_NOTHING)
    comments = models.CharField(max_length=255, null=True)
    created_on = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


    def get_absolute_url(self):
        return reverse('new-daily-activity')

