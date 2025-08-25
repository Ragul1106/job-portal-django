from django import forms
from .models import JobApplication
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us why you are interested in this position...'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'cover_letter',
            Submit('submit', 'Apply for Job', css_class='btn btn-primary')
        )
