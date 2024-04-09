from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic, View
from .models import Post


# Home Page View
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'bookings/index.html'
    paginate_by = 5

# /home page view

# Menu Page View
class PostDetail(generic.View):

    def menu(request):
        return render (
            request,
             'bookings/menu.html'
        )
# /menu page view

# Enquiries Page View
class PostDetail(generic.View):

    def enquiries(request):
        return render (
            request,
             'bookings/enquiries.html'
        )
# /enquiries page view


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