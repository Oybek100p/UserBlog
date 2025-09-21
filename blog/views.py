from django.shortcuts import render, get_object_or_404, redirect
from .models import Creator, Post
from .forms import CreatorForm, PostForm

# ==== CREATORS ====
def creator_list(request):
    creators = Creator.objects.all()
    return render(request, 'creators_list.html', {'creators': creators})

def creator_detail(request, pk):
    creator = get_object_or_404(Creator, pk=pk)
    return render(request, 'creator_detail.html', {'creator': creator})

def creator_create(request):
    if request.method == "POST":
        form = CreatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('creators')
    else:
        form = CreatorForm()
    return render(request, 'creator_form.html', {'form': form})

def creator_update(request, pk):
    creator = get_object_or_404(Creator, pk=pk)
    if request.method == "POST":
        form = CreatorForm(request.POST, request.FILES, instance=creator)
        if form.is_valid():
            form.save()
            return redirect('creator_detail', pk=creator.pk)
    else:
        form = CreatorForm(instance=creator)
    return render(request, 'creator_form.html', {'form': form})

def creator_delete(request, pk):
    creator = get_object_or_404(Creator, pk=pk)
    if request.method == "POST":
        creator.delete()
        return redirect('creators')
    return render(request, 'creator_confirm_delete.html', {'creator': creator})

# ==== POSTS ====
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('posts')
    return render(request, 'post_confirm_delete.html', {'post': post})
