from django.urls import path
from . import views
from .views import NewActivity, NewDailyActivity


urlpatterns = [
    path('', views.home, name='security-home'),
    path('new_activity', NewActivity.as_view(), name='new-activity'),
    path('new_daily_activity', NewDailyActivity.as_view(), name='new-daily-activity'),
]