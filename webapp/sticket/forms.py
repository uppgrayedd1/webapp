from django.forms import ModelForm
from .models import (
    Tickets,
)

from mgmt.models import (
    Departments,
    SubDepartments
)
class NewTicketForm(ModelForm):
    class Meta:
        model = Tickets
        fields = [
            'department_id',
            'sub_department_id',
            'category_id',
            'sub_category_id',
            'created_by_id',
            'ticket_name',
            'ticket_description',
            'property',
            'location',
        ]

    def __init__(self, department_id, *args, **kwargs):
        super(NewTicketForm, self).__init__(*args, **kwargs)
        self.fields['department_id'].queryset = SubDepartments.objects.filter(department_id=department_id)