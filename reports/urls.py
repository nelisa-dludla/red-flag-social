from django.urls import path
from .views import (
    IndexView,
    AboutView,
    SearchReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    UserReportListView
)


urlpatterns = [
    path('', IndexView.as_view(), name='reports-index'),
    path('about/', AboutView.as_view(), name='reports-about'),
    path('user/<str:username>/reports/', UserReportListView.as_view(), name='user-reports'),
    path('search/', SearchReportListView.as_view(), name='search_results'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
    path('report/new/', ReportCreateView.as_view(), name='report-create')
]
