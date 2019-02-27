from django.urls import path
from . import views
from .views import (
    TicketCreateView,
    AssignCreateView,
    StatusCreateView,
    StatusLstCreateView,
    CgyCreateView,
    CgyListView,
    TicketListView
)

urlpatterns = [
    path('', views.home, name='sticket-home'),
    path('categories', CgyListView.as_view(), name='categories'),
    path('new_stkt', TicketCreateView.as_view(), name='new-stkt'),
    path('new_assgn', AssignCreateView.as_view(), name='new-assgn'),
    path('new_status', StatusCreateView.as_view(), name='new-status'),
    path('add_status', StatusLstCreateView.as_view(), name='add-status'),
    path('add_cgy', CgyCreateView.as_view(), name='add-cgy'),
    path('ticket_list', TicketListView.as_view(), name='ticket_list')
]