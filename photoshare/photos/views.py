from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Category,Photo
from django.db.models import Q
# Create your views here.

def gallery(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    cat=Category.objects.all()
    # photos= Photo.objects.filter(Q(category__name__icontains=q)).select_related()
    photos= Photo.objects.filter(Q(category__name__contains=q))
    context={
        'category':cat,
        'photos':photos
    }
    return render(request,'photos/gallery.html',context) 
def photos(request,pk):
    photos= Photo.objects.get(id=pk)
    context={
        'photos':photos
    }
    return render(request,'photos/photo.html',context) 
def add(request):
    cat=Category.objects.all()
    if request.method=='POST':
        print(request.POST.get('category'))
        
        Photo.objects.create(
            category= Category.objects.get(id=int(request.POST.get('category'))),
            image=request.FILES.get('formFile'),
            description=request.POST.get('formText'),
        )
        return HttpResponseRedirect(reverse('photos:gallery'))
    context={
        'cats':cat,
    }
    return render(request,'photos/add.html',context) 