from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
)
from .models import Report

def index(request):
    context = {
        'title': 'Search'
    }
    return render(request, 'reports/index.html', context=context)

class ReportListView(ListView):
    model = Report
    template_name = 'reports/results.html'
    context_object_name = 'reports'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        reports = Report.objects.all()

        context = super().get_context_data(**kwargs)
        context['title'] = 'Results'
        context['reports'] = reports
        context['number_of_reports'] = reports.count()
        return context


class ReportDetailView(DetailView):
    model = Report


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = [
        'social_media_platform',
        'social_media_handle',
        'category',
        'description'
    ]

    def form_valid(self, form):
        form.instance.reported_by = self.request.user
        return super().form_valid(form)


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Report
    fields = [
        'social_media_platform',
        'social_media_handle',
        'category',
        'description'
    ]

    def form_valid(self, form):
        form.instance.reported_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.reported_by:
            return True
        return False


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Report
    success_url = '/'

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.reported_by:
            return True
        return False


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'reports/about.html', context=context)
