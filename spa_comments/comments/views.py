from django.shortcuts import render, redirect, HttpResponse
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
            return HttpResponse('Форма не є дійсною')
    else:
        form = CommentForm()
    return render(request, "base.html", {'form': form})
