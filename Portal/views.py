from django.shortcuts import render
from django.views.generic import ListView, FormView,DetailView, CreateView, UpdateView,DeleteView
from .models import *
from datetime import datetime
from .filters import ProductFilter
from .forms import *
from django.shortcuts import render, redirect
from django.http import *
from django.urls import reverse_lazy
from django.urls import reverse

class NewsList(ListView):
    model=Post
    ordering='-post_ID'
    template_name = 'news.html'
    context_object_name = 'Post'
    paginate_by=10
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['time_now']=datetime.utcnow()
        context['next_sale']=None
        return context


class NewsCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewsCreateForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'news_create.html'

    success_url = '/news/'

    def post(self, request):

        print(self.request.path)
        kwargs_upd = {'data': self.request.POST}

       # print(self.request.POST)
        post_type_tmp='ART' if self.request.path!='/news/create/' else 'NEWS'

        kwargs_upd["data"] = {'author_ID_FK': self.request.POST.get('author_ID_FK'),
                              'category_ID_FK': self.request.POST.getlist('category_ID_FK'),
                              'post_title': self.request.POST.get('post_title'),
                              'post_content': self.request.POST.get('post_content'),
                              'post_rank': self.request.POST.get('post_rank')}
       # print(kwargs_upd)
        form=NewsCreateForm(**kwargs_upd)

        if self.request.method == 'POST':
            try:
                if form.is_valid():
                    tx = form.save(commit=False)
                    tx.post_type= post_type_tmp
                    tx.save()
                    print('ok')
                else:
                    print(form.errors)
            except Exception as e:
                print(f'error:{e}')

        return redirect(reverse('news_list'))

class NewsEdit(UpdateView):
    form_class=NewsCreateForm
    model=Post
    template_name='news_edit.html'
    success_url = '/news/'

class NewsDelete(DeleteView):

    model = Post
    template_name = 'news_delete.html'
    success_url = '/news/'

class NewsSearch(ListView):
    model = Post
    ordering = '-post_ID'
    template_name = 'news_search.html'
    context_object_name = 'Post'
    paginate_by = 10

    def get_queryset(self):
        queryset=super().get_queryset()
        self.filterset=ProductFilter(self.request.GET,queryset)
        return self.filterset.qs

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['filterset'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        
        return context

class NewsListDetailed(DetailView):
    model=Post
    ordering='post_ID'
    template_name = 'news_detailed.html'
    context_object_name = 'Post'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['time_now']=datetime.utcnow()
        context['next_sale']=None

        return context
