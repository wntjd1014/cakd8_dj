from django.shortcuts import render
from blog.models import Post

# 이걸 클라이언트에게 보여주는거다.
def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'homepage/landing.html',
        {
            'recent_posts': recent_posts, 
        }
    )

def about_me(request):
    return render(
        request,
        'homepage/about_me.html'
    )