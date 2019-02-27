from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('add-cgy')


class Tickets(models.Model):
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey('mgmt.Departments', null=False, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Categories, null=False, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    ticket_name = models.CharField(max_length=50, null=False)
    ticket_description = models.CharField(max_length=255, blank=True, null=True)
    property = models.ForeignKey('mgmt.Properties', null=True, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=50, null=False)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ticket_name


    def get_absolute_url(self):
        return reverse('new-stkt')


class Assignments(models.Model):
    id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(Tickets, null=False, on_delete=models.DO_NOTHING)
    assigned_by = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING, related_name='assigned_by_id')
    assigned_to = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING, related_name='assigned_to_id')
    assigned_on = models.DateTimeField(default=timezone.now, null=False)


    def get_absolute_url(self):
        return reverse('new-assgn')


class StatusesList(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('add-status')


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    assignment = models.ForeignKey(Assignments, null=False, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, null=False, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(StatusesList, null=False, on_delete=models.DO_NOTHING, related_name='status_id')
    status_notes = models.CharField(max_length=255, blank=True, null=True)
    updated_on = models.DateTimeField(default=timezone.now, null=False)


    def get_absolute_url(self):
        return reverse('new-status')

