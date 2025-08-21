from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Follow, Comment
from django.contrib.auth.models import User
from .forms import PostForm


@login_required(login_url='login')
def base(request):
    user = request.user
    return render(request, 'base2.html', {user:"user"})

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all().order_by('-created_at')

    query = request.GET.get('q', '')
    user_results = User.objects.all()
    post_results = Post.objects.all()

    if query:
        user_results = user_results.filter(username__icontains=query)
        post_results = post_results.filter(caption__icontains=query)  # Change 'caption' to your post text field name

    # Mark each post as liked/unliked by current user
    for post in posts:
        post.is_liked = post.likes.filter(id=request.user.id).exists()

    context = {
        'posts': posts,
        'user_results': user_results,
        'post_results': post_results
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
def profile(request, user):
    profile_user = get_object_or_404(User, username=user)
    posts = Post.objects.filter(user__username=profile_user.username)
    no_of_post = posts.count()

    profile_user = get_object_or_404(User, username=user)
    is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()

    context = {
        "profile_user":profile_user,
        "posts":posts,
        "nopost":no_of_post,
        'profile_user': profile_user,
        'is_following': is_following
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def create_post(request):

    if request.method == "POST":
        caption = request.POST.get("caption")
        img = request.FILES.get("image")
        
        if img:
            Post.objects.create(caption=caption, image=img, user=request.user)
            return redirect("/")

    return render(request, 'post.html')

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# Post Detail Page
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'edit_post.html', {'post': post})
@login_required
def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id, user=request.user)  # only own posts

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_edit', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form, 'post': post})
    


@login_required
def del_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Optional: ensure only the owner can delete
    if post.user.username != request.user:
        return redirect("home")

    post.delete()
    return redirect("home")

    
@login_required
def follow_user(request, username):
    target_user = get_object_or_404(User, username=username)

    if target_user == request.user:
        return redirect(f'profile/{request.user.username}', username=username)
    
    follow_relation = Follow.objects.filter(follower=request.user, following=target_user)
    
    if follow_relation.exists():
        follow_relation.delete()
    else:
        Follow.objects.create(follower=request.user, following=target_user)
    
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def add_comment(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        text = request.POST.get("comment")
        if text.strip():
            Comment.objects.create(post=post, user=request.user, text=text)
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))
 

# Create your views here.
