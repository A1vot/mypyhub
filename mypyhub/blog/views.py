from django.shortcuts import render

def index(request):
    template = "blog/index.html"
    return render(request, template)

def post_detail(request, id):
    template = "blog/detail.html"
    return render(request, template)

def category_posts(request, category_slug):
    template = "blog/category.html"
    return render(request, template)