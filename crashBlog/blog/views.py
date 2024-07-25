from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from .forms import CommentForm
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
        return redirect ('post_detail', post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/detail.html',{'post':post, 'form':form})
