from django import forms
from .models import Message, Forum


class MessageForm(forms.ModelForm):
    media = forms.FileField(required=False)

    class Meta:
        model = Message
        fields = ['text', 'media']


class CreateForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = '__all__'
        exclude = ['owner', 'members']