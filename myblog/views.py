from django.shortcuts import render, redirect
from .models import Post,Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, "myblog/index.html", {
        "posts": Post.objects.all()
    })



def details(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.post = post
            Comment.save()
            return redirect("details", slug= post.slug)
    else:
        form = CommentForm()

    return render(request, "myblog/details.html", {
        "slug": slug,
        "comment" : Comment,
        "post": post
    })