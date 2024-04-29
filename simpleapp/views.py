from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Product
from datetime import datetime
from .filters import ProductFilter
from .forms import *
from django.http import *
from django.urls import reverse_lazy

class ProductsList(ListView):
    model=Product
    ordering='name'
    template_name = 'product.html'
    context_object_name = 'products'
    paginate_by=2
    def get_queryset(self):
        queryset=super().get_queryset()
        self.filterset=ProductFilter(self.request.GET,queryset)
        return self.filterset.qs

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['time_now']=datetime.utcnow()
        context['filterset']=self.filterset
        context['next_sale']=None

        return context


class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'product_detail.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'products'


def create_product(request):
    form = ProductForm(request.POST)
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/products/')
    return render(request,'product_edit.html',{'form':form})

class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'product_edit.html'

class ProductUpdate(UpdateView):
    form_class=ProductForm
    model=Product
    template_name='product_edit.html'

class ProductDelete(DeleteView):
    model=Product
    template_name='product_delete.html'
    success_url=reverse_lazy('product_list')