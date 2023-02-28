from django.db import models
from users.models import UsersModel

class CommentsModels(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)

class ReplyCommentsModels(models.Model):
    user = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentsModels, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)