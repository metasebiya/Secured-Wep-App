from django import forms
from django.forms import ModelForm

from feedback.models import Feedbacks


class FeedbackForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(required=False)

    class Meta:
        model = Feedbacks
        fields = ['username', 'email', 'content', 'file']
