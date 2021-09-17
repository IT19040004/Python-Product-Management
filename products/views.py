from django.shortcuts import render, redirect

# Create your views here.
import products
from . models import Product
from . forms import ProductForm


def ShowAllProducts(request):

    products = Product.objects.all()

    context = {

        'products' : products

    }

    return render(request, 'showProducts.html', context)



def productDetail(request, pk):

    eachproduct = Product.objects.get(id=pk)

    context = {

        'eachproduct' : eachproduct


    }

    return render(request, 'productDetail.html', context)


def addProduct(request):

        form = ProductForm()

        if request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():

                form.save()

                return redirect('showProducts')
        else:

            form = ProductForm()

        context ={

            "form":form

        }

        return render(request, 'addProduct.html', context)



