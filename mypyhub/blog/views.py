from django.shortcuts import render

posts = [
    {
        "id": 0,
        "status": "Не понимаю, почему Django не видит шаблон",
        "date": "15 мая 2026 года",
        "category": "django",
        "text": """Сегодня долго разбирался, почему Django упорно выдаёт TemplateDoesNotExist.
                Оказалось, что я создал папку templates внутри приложения, но забыл
                прописать путь в DIRS в настройках. Добавил — и всё заработало.
                В очередной раз убедился, что мелочи решают всё.""",
    },
    {
        "id": 1,
        "status": "Разобрался с миграциями и наконец всё работает",
        "date": "16 мая 2026 года",
        "category": "databases",
        "text": """Поймал странную ошибку с миграциями: Django ругался на конфликт
                зависимостей. Оказалось, что я изменил модель, но забыл удалить
                старую миграцию, которая конфликтовала с новой. Пересоздал миграции —
                и база поднялась без проблем. Полдня ушло, но результат радует.""",
    },
    {
        "id": 2,
        "status": "Сделал первый рабочий REST‑эндпоинт",
        "date": "17 мая 2026 года",
        "category": "rest-api",
        "text": """Сегодня наконец-то сделал свой первый полноценный REST‑эндпоинт.
                Подключил сериализатор, настроил вьюшку и протестировал через Postman.
                Получилось аккуратно и понятно. Теперь можно двигаться дальше и
                строить полноценный API.""",
    },
]


def index(request):
    template = "blog/index.html"
    context = {
        "posts": posts,
    }
    return render(request, template, context)


def post_detail(request, id):
    template = "blog/detail.html"
    context = {"post": posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = "blog/category_posts.html"
    context = {
        "posts": [post for post in posts if post["category"] == category_slug],
        "category": category_slug
        }
    return render(request, template, context)
