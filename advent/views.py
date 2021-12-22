import datetime

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View, DetailView, ListView
from django.urls import reverse

from .models import Comment, Date

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        context['user'] = self.request.user
        return context    

    def get_object(self, queryset=None):
        day = self.kwargs['day']
        month = self.kwargs['month']
        date = Date.objects.get(date__day=day, date__month=month)
        return date

    def post(self, request, **kwargs):
        if request.POST.get('comment'):
            date = self.get_object()
            Comment.objects.create(
                date=date,
                comment=request.POST.get('comment'))
            messages.success(request, 'Message received, thanks!')
            return redirect(reverse('date_list'))