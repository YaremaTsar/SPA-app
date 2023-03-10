from django import forms
from .models import CommentsModels
from captcha.fields import CaptchaField
from django.core.validators import EmailValidator

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModels
        fields = ["user", "text"]
        captcha = CaptchaField()
        email = forms.EmailField(validators=[EmailValidator(message='Введіть коректний email адрес.')])
        widgets = {
            'user': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }
    def save(self, commit=True, user=None):
        comment = super().save(commit=False)
        comment.user = user
        if commit:
            comment.save()
        return comment

