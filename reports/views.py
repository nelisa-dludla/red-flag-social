from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
        View
)
from .models import Report
from .forms import ReportForm


class IndexView(View):
    template_name = 'reports/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Search'
        }
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'reports/about.html'

    def get(self, request, *args, **kwargs):
        context = {
            'title': 'About'
        }
        return render(request, self.template_name, context)


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
            object_list = Report.objects.filter(social_media_handle__iexact=query)
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
    form_class = ReportForm

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
