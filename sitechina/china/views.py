from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name':
            'add_page'},
        {'title': "Обратная связь", 'url_name':
            'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Государство Шан', 'content':
        '''Государство Шан, впоследствии чжоусцы стали назвать его Инь, (иероглиф, обозначающий слово «государство»), возникло в XVIII в. до н. э. Шанцы занимались земледелием. Выращивали пшеницу, ячмень, бобы,
фасоль, коноплю, чумизу, овощи, фрукты. Появляется рис. Шанцы знали
то, что не знал никто мире – шелководство – уникальное китайское изобретение. Развитым было ремесло. Сохранились остатки керамических,
камнерезных, бронзолитейных и иных мастерских. Шанцам были известны
ирригация, строительство методом утрамбовки земли в опалубке и литей-
17
ное производство. Их также считают зачинателями китайской письменности. ''', 'is_published': True, 'category': 1},
    {'id': 2, 'title': 'Западное Чжоу', 'content':
        '''После падения династии Шан наступил период Чжоу, продолжавшийся 800 лет, но только 300 из них чжоуские цари обладали реальной
властью. Эпоха Чжоу подразделяется на Западное Чжоу (XII–VIII вв. до н.
э.) и Восточное Чжоу (VIII–III вв. до н. э.). Среди бесчисленного количества династий, правивших в мире, Чжоу является одной из самых уникальных. Она одна из самых долго царствовавших. В период Чжоу в Китае
происходит становление государственной власти, формируется система
управления, идет становление бюрократии.''', 'is_published': True,  'category': 1},

    {'id': 3, 'title': 'Период Чжаньго («Борющиеся царства», V–III вв. до н. э.)', 'content':
        '''Период Чжаньго был временем, сосуществования и междоусобной
борьбы семи крупнейших царств Вэй, Чжао, Хань, Цинь, Ци, Янь и Чу.
Царства Вэй, Чжао и Хань занимали территорию некогда могущественного
царства Цзинь, распавшегося в 403 г. до н. э. в результате борьбы аристократических родов. Их территории, являлись районом древнейшего расселения китайских племен и были наиболее заселенными. Земли этих царств
были богаты залежами металлических руд. Впервые железо стало добываться и обрабатываться в царстве Цзинь. Железо из Хань славилось по
всему Китаю. Наиболее крупным и сильным в военном отношении было
царство Чжао. Укреплению царства Чу способствовали реформы, направленные против родовой аристократии. В IV в. до н. э. Чу стало самым могущественным из семи царств. Его территория была расположена в бассейне рек Хуанхэ и Янцзыцзян и охватывала более трети той площади, которую занимали все остальные царства в целом. Царство Чу было богато
лесом, месторождениями железа, олова, меди и золота. В нем были разви-
34
ты ремесла. Период Чжаньго был периодом расцвета его культуры, которая оказала влияние на весь Южный Китай.''', 'is_published': True,  'category': 1},
{'id': 4, 'title': 'Шэньян', 'content':
        '''Сейчас Шэньян — это мегаполис, население которого превышает 7,5 млн человек. 
        Он является административным центром провинции Ляонин, крупным транспортным узлом, 
        а также важной промышленной базой в масштабах всей страны. 
        Нынешним названием Шэньян обязан географическому расположению. Город находится на северном берегу реки Хуньхэ, 
        которая в древности называлась Шэньшуй (沈水 Shěnshuǐ). В соответствии с традиционными принципами о сторонах света, 
        местность к северу от водоема называли «ян» (水北为阳 shuǐ běi wèi yáng). 
        Так из комбинации слогов и появился Шэньян (沈阳 Shěnyáng).''', 'is_published': True,  'category': 2},
{'id': 5, 'title': 'Шанхай', 'content':
        '''Шанха́й (кит. 上海, пиньинь Shànghǎi; у 上海 [zãhe], Zånhae) — основан в 751 году, 
        один из четырёх городов центрального подчинения КНР; расположен на востоке страны, в дельте реки Янцзы. 
        Важный культурный центр страны, а также крупнейший в мире морской порт. 
        Кроме того, Шанхай является крупнейшим финансовым центром Китая (опережая Пекин и Гонконг).
        Площадь Шанхая составляет 6340,5 кв. км.
         ''', 'is_published': True,  'category': 2},
{'id': 6, 'title': 'Гуандун', 'content':
        '''Прибрежная провинция на юго-востоке Китая. Ее южная часть омывается Южно-китайским морем. 
        Это самая густонаселенная провинция Китая, в которой проживает свыше 100 миллионов человек. 
        Главный город провинции – Гуанчжоу. Крупнейшие города провинции: Шэньчжэнь, Фошань, Дунгуань. 
        Метро и линии скоростных поездов соединяют эти города в единую крупнейшую агломерацию мира. 
        Для туристов эти города являются основными туристическими достопримечательностями. 
        Их привлекают многочисленные парки развлечений, фестивали, шопинг. 
        Помимо городов, посетителей ждут живописные виды гор, холмов, морского побережья и многочисленных рек.
         ''', 'is_published': True,  'category': 3},
{'id': 7, 'title': 'Шаньдун', 'content':
        '''Прибрежная провинция на востоке Китая. Столица Цзинань находится всего в 2-3 часах езды от Пекина и Шанхая на скоростном поезде. 
        Шаньдун – центр даосизма, китайского буддизма и конфуцианства. 
        Для туристов основными достопримечательностями являются религиозные памятники и храмы, а также пляжи и курорты Желтого моря и Бохайского залива. 
        Шаньдун имеет два объекта всемирного наследия ЮНЕСКО. Это место в городе Цюйфу, где жил и похоронен Конфуций и священная гора Тайшань – одна из пяти Великих гор даосизма в Китае. 
        Крупнейший в регионе город Циндао удивит гостей своей необычной архитектурой
         ''', 'is_published': True,  'category': 3},
]
cats_db = [
    {'id': 1, 'name': 'Династии'},
    {'id': 2, 'name': 'Города'},
    {'id': 3, 'name': 'Провинции'},
]


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,

    }
    return render(request, 'china/index.html',
                  context=data)


def about(request):
    return render(request, 'china/about.html',
                  {'title': 'О сайте', 'menu': menu})


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
    data = {
        'title': 'Поиск статьи',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,  # не обязательная строчка
    }
    return render(request, 'china/find.html',
                  context=data)


def show_post(request, post_id):
    #post = next((post for post in data_db if post['id'] == post_id), None)
    data = {
        'title': f"Отображение статьи с id = {post_id} ",
        'menu': menu,
        'posts': data_db,
        'post': post_id

    }
    return render(request, 'china/content.html',
                  context=data)
    '''if post:
        return render(request, 'content.html', {'menu': menu, 'post': post})
    else:
        return HttpResponse("Статья не найдена.")'''
   # return HttpResponse(f"Отображение статьи с id = {post_id} ")


def addpage(request):
    return render(request, 'china/add.html',
                  {'title': 'Добавить свою статью', 'menu': menu})


def contact(request):
    return render(request, 'china/contact.html',
                  {'title': 'Обратная связь', 'menu': menu})


def login(request):
    return render(request, 'china/login.html',
                  {'title': 'Вход', 'menu': menu})


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'china/cats.html',
                  context=data)
