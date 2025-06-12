from django.shortcuts import render,redirect
from .models import product
from .forms import productForm


# Create your views here.
def home(request):
    prod = product.objects.all()
    fm= productForm()
    if request.method =="POST":
        fm=productForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect ("home")
    else:
        fm=productForm()
        
    return render(request, 'Electronics/home.html', {'prod':prod, 'fm':fm})


def edit_product(request, product_id):
    product_instance = product.objects.get(id=product_id)
    
    if request.method == "POST":
        form = productForm(request.POST, instance=product_instance)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = productForm(instance=product_instance)
    
    return render(request, 'Electronics/edit_product.html', {'form': form})

def delete_product(request, product_id):
    product1 = product.objects.get(id=product_id)
    if request.method == "POST":
        product1.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html', {'product': product1})

