from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .form import registerform, proform
from .functions import handel_uploaded_file
from .models import Register, Product


def hi(request):
    return HttpResponse('<h1>hiii</h1>')
def register(request):
    if request.method == 'POST':
        form=registerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/login/')
            except:
                pass

        else:
            pass
    else:
         form=registerform()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method=='POST':
        u=request.POST.get('user_name')
        p=request.POST.get('Password')
        user=Register.objects.filter(user_name=u,Password=p).count()

        if user==1:
            un=Register.objects.filter(user_name=u,Password=p)
            for data in un:
                request.session['user_name'] = data.user_name
                request.session['id'] = data.id
                return redirect('/insert/')
        else:
            messages.error(request, 'Invalid username and password')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def insert(request):
    if request.method == 'POST':
        print(request.POST);
        print(request.FILES);
        form=proform(request.POST,request.FILES)
        if form.is_valid():
            try:
                handel_uploaded_file(request.FILES['pimage'])
                form.save()
                return redirect('/blog/')
            except:
                pass

        else:
            pass
    else:
         form=proform()
    return render(request,'insert.html',{'form':form})



def blog(request):
    p=Product.objects.all()
    return render(request,'blog.html',{'p':p})

def delete(request,id):
    p=Product.objects.get(id=id)
    p.delete()
    return redirect('/blog/')
def edit(request,id):
    p=Product.objects.get(id=id)
    return render(request, 'edit.html', {'p': p})

def update(request,id):
    p = Product.objects.get(id=id)
    if request.method == 'POST':
        form = proform(request.POST, instance=p)
        if form.is_valid():
            try:
                form.save()
                return redirect('/blog/')
            except:
                pass
        else:
            pass
    return render(request, 'edit.html', {'p': p})



def blog_detail(request, id):
    p = Product.objects.get(id=id)
    return render(request,'blog_detail.html',{'p':p})