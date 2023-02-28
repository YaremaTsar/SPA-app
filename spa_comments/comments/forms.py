from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModels
        fields = ["user", "email", "text", "object_id"]
        widgets = {
            "object_id": forms.HiddenInput()
        }

    def save(self, commit=True, user=None):
        comment = super().save(commit=False)
        comment.user = user
        if commit:
            comment.save()
        return comment

class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModels
        fields = ["name", "email", "text", "comment_parent"]
        widgets = {
            "comment_parent": forms.HiddenInput()
        }

    def save(self, commit=True, user=None):
        comment = super().save(commit=False)
        comment.user = user
        if commit:
            comment.save()
        return comment

