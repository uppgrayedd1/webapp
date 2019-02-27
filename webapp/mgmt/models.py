from django.db import models
from django.urls import reverse
from django.utils import timezone


class Properties(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    address_1 = models.CharField(max_length=255, null=False)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, default="Lancaster", null=False)
    state = models.CharField(max_length=2, default="PA", null=False)
    zip = models.IntegerField(default=17603, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add-prop')


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add-dept')


class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(Departments, null=False, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    hire_date = models.DateField(null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('add-emp')




