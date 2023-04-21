from django.shortcuts import render, redirect
from .forms import ProductForm
from django.utils import timezone
from .models import Product
from django.contrib.auth.decorators import login_required



@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            form.add_timestamps()
            return redirect('sellerhome')
    else:
        form = ProductForm(user=request.user)
    return render(request, 'create_product.html', {'form': form})



#27th march 12.14am
def deactivate(request):
    # clear current session
    request.session.flush()
    return redirect('home')


def viewp(request):
    form = ProductForm(initial={'user':'', 'name': '', 'price': '', 'image': None, 'quantity': '', 'description': '', 'meta_keywords': '', 'category': None})
    return render(request,'seller-profile.html', form)

def addp(request):
    form = ProductForm(initial={ 'name': '', 'price': '', 'image': None, 'quantity': '', 'description': '', 'meta_keywords': '', 'category': None})
    return render(request,'create_product.html', form)

