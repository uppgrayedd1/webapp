from django.shortcuts import render
from django.views.generic import CreateView
from .models import (
    Departments,
    Employees,
    Properties,
)

# Create your views here.
def home(request):
    return render(request, 'mgmt/home.html')


class DptCreateView(CreateView):
    model = Departments
    fields = ['name']


class EmpCreateView(CreateView):
    model = Employees
    fields = [
        'first_name',
        'last_name',
        'email',
        'department_id',
        'hire_date'
    ]


class PropCreateView(CreateView):
    model = Properties
    fields = [
        'name',
        'address_1',
        'address_2',
        'city',
        'state',
        'zip'
    ]