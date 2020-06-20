from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    """
    С помощью класса List View заменяем Index
    model - получаем список всех новостей
    template_name - устанавливаем нужную нам страницу
    get_context_data - присваем нужные нам значения в context
    get_queryset -  получаем нужный нам отфильтрованный набор объектов
    """
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)



# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context )

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', { 'news': news, 'category': category } )

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid(): # если форма прошла валидацию
            # print(form.cleaned_data) # если данные прошли валидацию данные попадают в словарь clean_data
            # title = form.cleaned_data('tilte') # неудобный способ
            # News.objects.create(title=title) # неудобный способ
            # news = News.objects.create(**form.cleaned_data) # распаковка словарей используется две звездочки (**)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})