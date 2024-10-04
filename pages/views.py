from django.shortcuts import render
from .models import BlogPost, Comment
from .serializer import BlogSerializer

# Create your views here.
def homepage(request):
    blogs = BlogPost.objects.all()
    data  = {
        'blogPosts' : blogs,
    }
    return render(request, 'index.html',data)


def readblog(request,key):
    blog = BlogPost.objects.get(id = key)
    if(request.method == 'POST'):
        c = request.POST['comment']
        u = request.POST['user']
        Comment.objects.create(blog_post = blog, user = u, comment = c)
    data = {
        'blog' : blog,
        'comments': blog.comments.all()
        }
    return render(request, 'readblogpost.html',data)
    


def newblog(request):
    if(request.method == 'POST'):
        title = request.POST['blogtitle']
        content = request.POST['blogcontent']
        BlogPost.objects.create(title = title, content = content)

    return render(request, 'newblogpost.html')


