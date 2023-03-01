from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class CommentsModels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments_user_group', related_query_name='comment')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, null=True, default=None)

    def __str__(self):
        return self.text


