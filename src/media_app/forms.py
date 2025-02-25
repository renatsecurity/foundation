from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for comments to the news."""
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'name': 'name',
                'class': 'form-control',
                'placeholder': 'Your Name*',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'name': 'email',
                'class': 'form-control',
                'placeholder': 'Your Email*',
                'required': True,
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'name': 'comment_submit',
                'rows': 6,
                'placeholder': 'Your Comment*',
                'required': True,
            }),
        }


class ReplyForm(forms.ModelForm):
    """Form for comments to the parent comment."""

    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'type': 'text',
                'name': 'name',
                'class': 'form-control',
                'placeholder': 'Your Name*',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'name': 'email',
                'class': 'form-control',
                'placeholder': 'Your Email*',
                'required': True,
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'name': 'reply_submit',
                'rows': 6,
                'placeholder': 'Reply...',
                'required': True,
            }),
        }
