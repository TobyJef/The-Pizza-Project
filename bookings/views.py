from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 5

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        quereyset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            "post_review.html",
            {
                "post": post,
                "comments": comments
            }
        )