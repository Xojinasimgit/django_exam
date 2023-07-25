from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.forms import RegisterForm, CategoryForm, BlogForm, CommentForm, EmailForm
from apps.models import User, Category, Blog, Comment


# Create your views here.

def index(request):
    agent = User.objects.all()
    categories = Category.objects.all()
    blog = Blog.objects.all()
    return render(request, 'index.html', {'agent': agent, 'categories': categories, 'blog': blog})


def about(request):
    agents = User.objects.all()
    categories = Category.objects.all()
    return render(request, 'about.html', {'agents': agents, 'categories': categories})


def agent_single(request, pk):
    categories = Category.objects.filter(author_id=pk).all()
    ct = User.objects.filter(id=pk).first()
    agent_cate_count = Category.objects.filter(author_id=ct).count()
    return render(request, 'agent-single.html',
                  {'ct': ct, 'agent_cate_count': agent_cate_count,
                   'categories': categories})


def agents_grid(request):
    categories = Category.objects.all()
    agents = User.objects.all()
    category1 = Category.objects.all()
    paginator = Paginator(category1, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'agents-grid.html', {'agents': agents, 'categories': categories, 'page_obj': page_obj})


def blog_grid(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    return render(request, 'blog-grid.html', {'blogs': blogs, 'categories': categories})


def blog_single(request, pk):
    categories = Category.objects.all()
    blog = Blog.objects.filter(id=pk).first()
    agent = User.objects.filter(id=blog.author_id).first()
    comment = Comment.objects.filter(to_blog=pk)
    comments_count = Comment.objects.filter(to_blog=pk).count()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.to_blog = blog
            form.save()
            return redirect(reverse('blog_single', args=(pk,)))
    return render(request, 'blog-single.html',
                  {'blog': blog, 'agent': agent, 'comment': comment, 'comment_count': comments_count,
                   'categories': categories})


def contact(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email_sender = form.save()
            subject = 'Email from {}'.format(email_sender.name)
            sender = email_sender.email
            message = f"from: {sender} Text: {email_sender.text}"
            recipient_list = ['xbobonazarov0555@gmail.com']
            send_mail(subject, message, request.POST.get('email'), recipient_list)
            return redirect('index')
        if form.errors:
            print(form.errors.as_json(escape_html=True))
    else:
        form = EmailForm()
    return render(request, 'contact.html', {'form': form, 'categories': categories})


def property_grid(request):
    categories = Category.objects.all()
    category = Category.objects.all()
    if request.method == 'GET':
        type = request.GET.get('type')
        beds = request.GET.get('beds')
        baths = request.GET.get('baths')
        city = request.GET.get('city')
        garages = request.GET.get('garages')
        price = request.GET.get('price')
        if type:
            category = category.filter(property_Type=type)
        if beds:
            category = category.filter(beds=beds)
        if baths:
            category = category.filter(baths=baths)
        if city:
            category = category.filter(location=city)
        if garages:
            category = category.filter(garages=garages)
        if price:
            category = category.filter(price=price)

    category1 = Category.objects.all()
    paginator = Paginator(category1, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'property-grid.html', {'category': category, 'categories': categories, 'page_obj': page_obj})


@login_required
def property_single(request, pk):
    categories = Category.objects.all()
    category = Category.objects.filter(id=pk).first()
    agent = User.objects.filter(id=category.author_id).first()
    return render(request, 'property-single.html', {'category': category, 'agent': agent, 'categories': categories})


def signup(request):
    if request.POST:
        form = RegisterForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        if errors := form.errors:
            print(errors.as_json(escape_html=True))
            return render(request, 'signup.html', {'errors': errors})
    return render(request, 'signup.html')


def signin(request):
    data = request.POST
    if data:
        username = data.get('username')
        password = data.get('password')
        valid = authenticate(username=username, password=password)
        if valid:
            login(request, valid)
            return redirect('index')
    return render(request, 'signin.html')


def add_category(request):
    if request.POST:
        data = request.POST.copy()
        data['author'] = request.user
        cate = CategoryForm(data=data, files=request.FILES)
        if cate.is_valid():
            cate.save()
            return redirect('index')
        if errors := cate.errors:
            print(errors.as_json(escape_html=True))
            return render(request, 'add_category.html', {'errors': errors})
    return render(request, 'add_category.html')


def add_blog(request):
    if request.POST:
        data = request.POST.copy()
        data['author'] = request.user
        blog = BlogForm(data=data, files=request.FILES)
        if blog.is_valid():
            blog.save()
            return redirect('index')
        if errors := blog.errors:
            print(errors.as_json(escape_html=True))
            return render(request, 'add_blog.html', {'errors': errors})
    return render(request, 'add_blog.html')


def log_out(request):
    logout(request)
    return redirect('index')
