from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    ListView
)
from .models import (
    Tickets,
    Assignments,
    Status,
    StatusesList,
    Categories
)


def home(request):
    return render(request, 'sticket/home.html')


def categories(request):
    context = {
        'categories': Categories.objects.all()
    }
    print(context)
    return render(request, 'sticket/categories.html', context)

class TicketCreateView(CreateView):
    model = Tickets
    fields = [
        'department',
        'category',
        'ticket_name',
        'ticket_description',
        'property',
        'location',
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AssignCreateView(CreateView):
    model = Assignments
    fields = [
        'ticket',
        'assigned_to',
    ]

    def form_valid(self, form):
        form.instance.assigned_by = self.request.user
        return super().form_valid(form)


class StatusCreateView(CreateView):
    model = Status
    fields = [
        'assignment',
        'status',
        'status_notes',
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# Status-lists Views
class StatusLstCreateView(CreateView):
    model = StatusesList
    fields = [
        'status',
    ]

# Category Views
class CgyListView(ListView):
    model = Categories
    template_name = 'sticket/categories.html'
    context_object_name = 'categories'
    ordering = ['category']

class CgyCreateView(CreateView):
    model = Categories
    fields = [
        'category',
    ]

class TicketListView(ListView):
    model = Tickets
    template_name = 'sticket/ticketlist_form.html'
    context_object_name = 'tickets'
    ordering = ['ticket_name']



