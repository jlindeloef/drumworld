from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic, View
from .models import Post, Category, Comment
from .forms import CommentForm
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

"""
The created posts
"""
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

"""
The comment and likes and info of post
"""
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.writer = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

"""
The like function
"""
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

"""
The categories
"""
class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs
                                        ['category']).filter(status='1')
        }
        return content


def category_list(request):
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }
    return context

"""
The edit omment view
"""
class CommentUpdateView(SuccessMessageMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "edit_comment.html"
    success_message = "You updated your comment successfully"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})

"""
The delete comment view
"""
class CommentDeleteView(SuccessMessageMixin, DeleteView):
    model = Comment
    form_class = CommentForm
    template_name = 'delete_comment.html'
    success_message = "You deleted your comment successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CommentDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.post.slug})
        






    












