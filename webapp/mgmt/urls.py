from django.urls import path
from . import views
from .views import (
    DptCreateView,
    EmpCreateView,
    PropCreateView,
)


urlpatterns = [
    path('', views.home, name='mgmt-home'),
    path('add_dept', DptCreateView.as_view(), name='add-dept'),
    path('add_emp', EmpCreateView.as_view(), name='add-emp'),
    path('add_prop', PropCreateView.as_view(), name='add-prop'),
]