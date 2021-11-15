import datetime

from django.shortcuts import render
from django.views.generic import View, DetailView, ListView

from .models import Date

class DateList(ListView):
    model = Date

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calendar'] = self.get_calendar()
        context['today'] = datetime.date.today()
        return context

    def get_calendar(self):
        calendar = []
        weeks = range(6)
        start_date = datetime.date(2021,11,15)
        for week in weeks:
            weekstart = start_date + datetime.timedelta(days=week*7)
            date_list = [weekstart + datetime.timedelta(
                days=x) for x in range(7)]
            calendar.append(date_list)
        return calendar


class DateDetail(DetailView):
    model = Date

    def get_object(self, queryset=None):
        day = self.kwargs['day']
        month = self.kwargs['month']
        date = Date.objects.get(date__day=day, date__month=month)
        return date