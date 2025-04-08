from django import forms

from .models import Support


class SupportForm(forms.ModelForm):
    template_name = "form_snippet.html"
    
    class Meta:
        model = Support
        fields =  ("username", "email", "text")