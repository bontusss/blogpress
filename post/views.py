from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from taggit.models import Tag

from post.models import Post

# Create your views here.
class postListView(ListView):
    pass


#     queryset = Post.objects.filter(status='published')
#     context_object_name = 'posts'
#     paginate_by = 6
#     template_name = 'post_list.html'


#     def get_context_data(self, **kwargs):
#         context =  super(postListView, self).get_context_data(**kwargs)
#         context['latest_posts'] = Post.objects.filter(status='published')[:3]
#         return context


def post_list(request, tag_slug=None):
    object_list = Post.objects.filter(status="published")
    latest_posts = Post.objects.filter(status="published")[:3]
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        "post_list.html",
        {"page": page, "posts": posts, "tag": tag, "latest_posts": latest_posts},
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "post_detail.html", {"post": post})


def index(request):
    latest_posts = Post.objects.filter(status="published")[:3]
    featured_posts = Post.objects.filter(status="published", featured=True)[:3]
    context = {'fposts': featured_posts, 'lposts': latest_posts}
    return render(request, 'index.html', context)