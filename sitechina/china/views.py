from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
import uuid

from django.urls import reverse_lazy
from django.views.generic import CreateView

from china.forms import AddPostForm, UploadFileForm
from china.models import China, Category, TagPost, UploadFiles

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name':
            'add_page'},
        {'title': "Обратная связь", 'url_name':
            'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

cats_db = [
    {'id': 1, 'name': 'История'},
    {'id': 2, 'name': 'Города'},
    {'id': 3, 'name': 'Провинции'},
    {'id': 4, 'name': 'Личности'},
    {'id': 5, 'name': 'Праздники'},
]


# Create your views here.

def index(request):
    posts = China.published.all()
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'china/index.html',
                  context=data)


def handle_uploaded_file(f):
    name = f.name
    ext = ''
    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]
    suffix = str(uuid.uuid4())
    with open(f"uploads/{name}_{suffix}{ext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()

    else:
        form = UploadFileForm()
    return render(request, 'china/about.html',
              {'title': 'О сайте', 'menu': menu, 'form': form})


def categories(request, cat_id):
    return HttpResponse("<h1>Статьи по категориям</h1><p >id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2024:
        return redirect(index, permanent=True)
    return HttpResponse(f"<h1>Архив событий по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def dictionary(request):
    return HttpResponse("<h1>Страница для словаря</h1>")


def find_information(request):
    posts = China.published.all()
    data = {
        'title': 'Поиск статьи',
        'menu': menu,
        'posts': posts,

    }
    return render(request, 'china/find.html',
                  context=data)


def show_post(request, post_slug):
    post = get_object_or_404(China, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,

    }
    return render(request, 'China/post.html',
                  context=data)


'''def show_post(request, post_id):
    #post = next((post for post in data_db if post['id'] == post_id), None)
    data = {
        'title': f"Отображение статьи с id = {post_id} ",
        'menu': menu,
        'posts': data_db,
        'post': post_id

    }
    return render(request, 'china/content.html',
                  context=data)
    if post:
        return render(request, 'content.html', {'menu': menu, 'post': post})
    else:
        return HttpResponse("Статья не найдена.")'''

# return HttpResponse(f"Отображение статьи с id = {post_id} ")

'''
def addpage(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            selected_categories = form.cleaned_data['Категории']
        return render(request, 'china/add.html',
                      {'title': 'Добавить свою статью', 'menu': menu, 'form': form})
    else:
        form = CategoryForm()
        return render(request, 'china/add.html',
                      {'title': 'Добавить свою статью', 'menu': menu, 'form': form})
'''


#
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#
#             title = request.POST.get('title')
#             slug = request.POST.get('slug')
#             content = request.POST.get('content')
#             cat_id = request.POST.get('category_id')
#
#            # Получите объект категории (category_instance) по cat_id
#
#             china_obj = China(title=title, slug=slug, content=content, cat=cat_id,
#                       is_published=China.Status.PUBLISHED)
#             china_obj.save()
#
#     # print(form.cleaned_data)
#             tag = request.POST.get('tags')
#             china_obj.tags.add(tag)
#             china_obj.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'china/addpage.html',
#               {'menu': menu, 'title': 'Добавление статьи', 'form':
#                   form})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'china/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'menu': menu,
        'title': 'Добавление статьи',
    }


"""
def process_add(request):
    if request.method == 'POST':
        title_p = request.POST.get('title_p')
        content_p = request.POST.get('content_p')
        annotation_p = request.POST.get('annotation_p')
        slug_p = request.POST.get('slug_p')
        form = CategoryForm(request.POST)
        if form.is_valid():
            selected_categories = form.cleaned_data['categories']

            w = China.objects.create(title=f'{title_p}', content=f'{content_p}', cat_id=int(selected_categories[0]),
                                     annotation=f'{annotation_p}',
                                     slug=f'{slug_p}')
            China.objects.filter(pk__lte=1).update(is_published=1)

        return render(request, 'china/add.html',
                      {'title': 'Добавить свою статью', 'message': 'Статья добавлена', 'menu': menu, 'form': form})

    else:
        form = CategoryForm()
        return render(request, 'china/add.html',
                      {'title': 'Добавить свою статью', 'menu': menu, 'form': form})
"""


def contact(request):
    return render(request, 'china/contact.html',
                  {'title': 'Обратная связь', 'menu': menu})


def login(request):
    return render(request, 'china/login.html',
                  {'title': 'Вход', 'menu': menu})


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = China.published.filter(cat_id=category.pk)
    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'china/index.html',
                  context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=China.Status.PUBLISHED)
    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'china/index.html', context=data)
