from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from apiapp.models import Book, Category, Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from .forms import createform
# from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"user/index.html")


class BookList(ListView):
    permission_classes = [IsAuthenticated]
    model = Book

class BookDetail(DetailView):
    permission_classes = [IsAuthenticated]
    model = Book

class ProductList(ListView):
    permission_classes = [IsAuthenticated]
    model = Product

class ProductDetail(DetailView):
    permission_classes = [IsAuthenticated]
    model = Product

class CategoryList(ListView):
    permission_classes = [IsAuthenticated]
    model = Category

class CategoryDetail(DetailView):
    permission_classes = [IsAuthenticated]
    model = Category
 

def my_login(request): 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect("home")
        else:
            messages.info(request, 'username or password is incorrect')
                 
    context = {}
    return render(request, 'user/login.html', context)

# @login_required(login_url='logg')
def register(request):
    form = createform()

    if request.method =="POST":
        form = createform(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('username')
            messages.success(request, f"Hey! {name}, your account was successfully created")
            return redirect('log')

    context = {
        'form':form
    }
    return render(request, 'user/register.html', context)

