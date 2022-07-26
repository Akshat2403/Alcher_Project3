from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'like': 5
    },
    {
        'like': 69
    },
    {
        'like': 1005
    },
    {
        'like': 420
    },
    {
        'like': 6234
    },
    {
        'like': 52
    },
    {
        'like': 62
    }

]
def home(request):
    return render(request, 'Project/index.html',{'title':'Login'})
def profile(request):
    return render(request, 'Project/index2.html',{'title':'Profile'})
def post(request):
    details={
        'posts' : posts,
        'title' : 'My Posts'
    }
    return render(request, 'Project/index4.html', details)
def create(request):
    return render(request, 'Project/index3.html', {'title':'New Post'})
# Create your views here.
