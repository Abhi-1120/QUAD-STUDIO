from django.shortcuts import render, redirect
from Studio.models import *
from .forms import ImageForm
from django.contrib.auth.decorators import login_required


def LoginPage(request):
    return render(request, "Studio/sign-in.html")


def RegisterPage(request):
    return render(request, "Studio/sign-up.html")


@login_required(redirect_field_name='login')
def Add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category,
                title=data['title'],
                images=image,
            )
    context = {'categories': categories, 'photo': photo}
    return render(request, 'Studio/add.html', context)


def Index(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.filter(main=True)
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    params = {'categories': categories, 'photos': photos}
    return render(request, "Studio/index.html", params)

def About(request):
    return render(request, "Studio/about.html")

def Services(request):
    return render(request, "Studio/services.html")

def Projects(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.filter(main=True)
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    params = {'categories': categories, 'photos': photos}
    return render(request, "Studio/projects.html", params)


def ProjectDetails(request, project_name):
    image = Photo.objects.filter(project_name=project_name)
    context = {'image': image}
    return render(request, "Studio/blog-details.html", context)


def Dashboard(request):
    photo = Photo.objects.all()
    params = {'photo': photo}
    return render(request, 'Studio/dashboard.html', params)


def Delete(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('/dashboard')
    context = {'photo': photo}
    return render(request, 'Studio/delete.html', context)


def Update(request, pk):
    photo = Photo.objects.get(id=pk)
    form = ImageForm(instance=photo)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    context = {'form': form, 'photo': photo}
    return render(request, 'Studio/update.html', context)


def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, 'Studio/contact.html')
