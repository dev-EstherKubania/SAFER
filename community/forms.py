from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    media = forms.FileField(required=False)

    class Meta:
        model = Message
        fields = ['text', 'media']