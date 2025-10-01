from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Traveller
from .forms import CommentForm, ProfileForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def traveller_profile(request, username):
    """
    view to display traveller profile page
    """
    user = get_object_or_404(User, username=username)
    traveller, created = Traveller.objects.get_or_create(user=user)
    
    return render(
        request,
        "blog/traveller_profile.html",
        {
            "traveller": traveller,
            "user": user,
        },
    )

@login_required
def edit_traveller_profile(request, username):
    """
    view to edit traveller profile
    """
    user = get_object_or_404(User, username=username)
    traveller, created = Traveller.objects.get_or_create(user=user)
    
    if request.user != traveller.user:
        messages.error(
            request,
            "You do not have permission to edit this profile"
        )
        return redirect("traveller_profile", username=username)
        
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=traveller)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect("traveller_profile", username=username)
        else:
            messages.error(request, "Error updating profile")
    else:
        form = ProfileForm(instance=traveller)
        
    return render(
        request,
        "blog/profile_form.html",
        {
            "form": form,
            "traveller": traveller
        }
    )