from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import Blog,BlogCategory,Comment
# Create your views here.
def index(request):
    # return HttpResponse("Hello World !!")
    return render(request,'blog/index.html')

def about(request):
    # return HttpResponse("<h1>About US</h1>")
    return render(request,'blog/about.html')

def contact(request):
    mobile = 9845671452
    email = "pulseai@gmail.com"
    a = 10
    b = 20
    languages = ['C','C++','Java','Python']
    blog = {
        "title":"Blog Title",
        "author":"John",
        "content":"Blog Details"
    }
    student = [
        {"roll":1,"name":"John","cgpa":8.9},
        {"roll":2,"name":"harry","cgpa":8.8},
        {"roll":3,"name":"Ram","cgpa":9.2},
        {"roll":4,"name":"Tom","cgpa":9.4},
        {"roll":5,"name":"CAT","cgpa":7.8}
    ]
    context = {
        "mob":mobile,
        "email":email,
        "a":a,
        "b":b,
        "languages":languages,
        'blog':blog,
        'students':student
    }
    return render(request,'blog/contact.html',context)

def all_blogs(request,cid=0):
    # blogs = Blog.objects.all()
    if cid ==0:
        blogs = Blog.objects.filter(publish=True).order_by('-update_at')
    else:
        blogs = Blog.objects.filter(publish=True,category=cid).order_by('-update_at')
    categories = BlogCategory.objects.all().order_by('category')
    context={
        'blogs':blogs,
        'categories':categories
    }
    return render(request,'blog/blog.html',context)


def blog_details(request,bid):
    # blog = Blog.objects.get(id=bid) gives individual items
    blog = get_object_or_404(Blog , pk=bid)
    comments = Comment.objects.filter(blog=blog).order_by("-created_at")
    context = {
        'blog':blog,
        'comments':comments
    }

    return render(request,'blog/details.html',context)

def comment(request):
    if request.method == "POST":
        user = request.user
        blog_id = request.POST.get('bid')
        comment = request.POST.get('comment')

        blog = Blog.objects.get(id=blog_id)

        comment = Comment(user=user, blog=blog, comment=comment)
        comment.save()
        return redirect('/blog/'+blog_id)
    