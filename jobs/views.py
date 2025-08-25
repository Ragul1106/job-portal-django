from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Job, JobApplication
from .forms import JobApplicationForm

class JobListView(ListView):
    model = Job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    paginate_by = 10
    
    def get_queryset(self):
        return Job.objects.filter(is_active=True)

class JobDetailView(DetailView):
    model = Job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['has_applied'] = JobApplication.objects.filter(
                job=self.object, 
                user=self.request.user
            ).exists()
            context['application_form'] = JobApplicationForm()
        return context

@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    
    # Check if user has already applied
    if JobApplication.objects.filter(job=job, user=request.user).exists():
        messages.warning(request, 'You have already applied for this job.')
        return redirect('jobs:job_detail', pk=pk)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            messages.success(request, f'Successfully applied for {job.title}!')
            return redirect('jobs:job_detail', pk=pk)
    
    return redirect('jobs:job_detail', pk=pk)

class AppliedJobsView(LoginRequiredMixin, ListView):
    template_name = 'jobs/applied_jobs.html'
    context_object_name = 'applications'
    paginate_by = 10
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)
