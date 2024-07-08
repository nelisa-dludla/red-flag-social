from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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

class SearchReportListView(ListView):
    model = Report
    template_name = 'reports/results.html'
    context_object_name = 'reports'
    ordering = ['-created_at']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Results'
        context['number_of_reports'] = context['reports'].count()
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Report.objects.filter(social_media_handle__icontains=query)
        else:
            object_list = Report.objects.none()
        return object_list


class UserReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/user_reports.html'
    context_object_name = 'reports'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Results'
        context['number_of_reports'] = context['reports'].count()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Report.objects.filter(reported_by=user).order_by('-created_at')

    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        if user != self.request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


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
