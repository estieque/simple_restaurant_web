from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost, PostAuthor, Comment, PostCategory
from restaurantWeb.models import SiteSetting
from seo.models import BlogPage
from sliders.models import blogSlider
from .views import *
# Create your views here.
def blog(request):
    blogs = BlogPost.objects.all()
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    authimage = PostAuthor.objects.all()
    settings = SiteSetting.objects.all()
    blogseo = BlogPage.objects.all().order_by('-id')[:1]
    blogslider = blogSlider.objects.all().order_by('-hslider_id')[:1]
    context = {'blogs':blogs, 'authimage':authimage, 'settings':settings, 'blogslider':blogslider, 'homeblogs':homeblogs, 'blogseo':blogseo,}
    return render(request, 'blog.html', context)




def blog_detail(request, slug_url):
    blogd = BlogPost.objects.get(slug=slug_url)
    homeblogs = BlogPost.objects.all().order_by('-add_date')[:3]
    authimage = PostAuthor.objects.all()
    settings = SiteSetting.objects.all()
    blogslider = blogSlider.objects.all().order_by('-hslider_id')[:1]
    comments = Comment.objects.all()
    if request.method=="POST":
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        content=request.POST.get('Content')
        en=Comment(name=name,email=email,content=content)
        en.save()
    
    context ={'blogd':blogd,'homeblogs':homeblogs, 'authimage':authimage, 'settings':settings, 'blogslider':blogslider,'comments':comments,}
    return render(request, "blog-single.html", context)