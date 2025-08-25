from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/apply/', views.apply_for_job, name='apply_job'),
    path('applied/', views.AppliedJobsView.as_view(), name='applied_jobs'),
]
