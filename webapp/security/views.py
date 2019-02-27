from django.shortcuts import render
from django.views.generic import CreateView
from .models import Activities, DailyActivity
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'security/home.html')



class NewActivity(CreateView):
    model = Activities
    fields = ['activity']



class NewDailyActivity(CreateView):
    model = DailyActivity
    fields = [
        'property',
        'activity',
        'comments',
    ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
