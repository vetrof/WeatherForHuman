from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView

from feel_data.models import FeelsData
from users.models import User

class FeelHistoryView(ListView):

    template_name = 'my_feel_history/feel_history.html'
    title = 'История'
    queryset = FeelsData.objects.all()
    ordering = ('-create_at')

    def get_queryset(self):
        queryset = super(FeelHistoryView, self).get_queryset()
        return queryset.filter(user=self.request.user)
