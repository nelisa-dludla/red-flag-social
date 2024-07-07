from django.urls import path
from .views import (
    ReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView
)

from . import views

urlpatterns = [
    path('', views.index, name='reports-index'),
    path('about/', views.about, name='reports-about'),
    path('results/', ReportListView.as_view(), name='results'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
    path('report/new/', ReportCreateView.as_view(), name='report-create')
]
