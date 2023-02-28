from django.shortcuts import render, redirect
from .models import CommentsModels
from .forms import CommentForm

def comment_create(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect("comments")
        else:
            form = CommentForm()
        return render(request, 'comments.html', {'form': form})