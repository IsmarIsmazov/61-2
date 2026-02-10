# # login = {"username": "Ismar", "password": "12345678"}
# # print(login)
# # username = login.get("name", "Что угодно")
# # print(username)

# slovar = {
#     "username": "Ismar",
#     "password": "12345678",
# }

# spisok = ["1234", 1, True]


# def func(*args):
#     print(args)


# func("username", "password")


# python manage.py startproject <name> . 
# python manage.py migrate
# python manage.py startapp 
# добавить приложение в settings.py
# прописать модельку для бд
# python manage.py makemigrations
# python manage.py migrate
# добавить модельку в админку
# python manage.py createsuperuser


# ---------

# создать файл forms.py
# создание класса
# прописать views
# html передаем во views
# csrf token внутри html 
# urls


# def get_all(request): views
#     if request.method == "GET":
#         return print("Hello")

# urlpatterns = []

# -------------- ORM ---------------
#  Model.objects.all()
#  Model.objects.filter(id=2).delete()
#  Model.objects.get(name="name") ТАК НЕ ПОЛУЧИТСЯ (если два и более обьекта)!
#  Model.objects.get(id=1) ВОТ ТАК ВОТ ПОЛУЧИТСЯ!

#  Model.objects.filter(name="name").update(name="username") Первый Способ


#. Второй способ 
#  model = Model.objects.all()
#  for i in model:
#      if i.name == "name":
    #      i.name = "Name"
    #      i.save()


# Model.objects.create(name="name", description="description")


# null=True, blank=True, default="Default value", unique=True

# -------------- TEMPLATES ---------------
# внутри метода render передавать context
# {{ product.name }} вызов value из context'а
# {% <method> %} методы внутри html
# {% extends 'base.html' %}
# {% block content %}
# {% endblock %}
# {% forms.as_p %}

# -------------- AUTH ---------------
# Аунтентификация - проверка пользователя в бд
# Авторизация - проверка прав
# Регистрация - создание нового пользователя в бд
# Users.objects.create_user()

# -------------- DATABASE --------------- 
# One2Many
# One2One
# Many2Many

# One2Many - ForeingKey(Model)
# Many2Many - ManyToManyField(Model) Промежуточная таблица
# One2One - OneToOneField(Model) 

# DDD