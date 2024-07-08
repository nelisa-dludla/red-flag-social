from django.urls import path
from .views import (
    SearchReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    UserReportListView
)

from . import views

urlpatterns = [
    path('', views.index, name='reports-index'),
    path('about/', views.about, name='reports-about'),
    path('user/<str:username>/reports/', UserReportListView.as_view(), name='user-reports'),
    path('search/', SearchReportListView.as_view(), name='search_results'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
    path('report/new/', ReportCreateView.as_view(), name='report-create')
]
