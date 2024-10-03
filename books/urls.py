from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books_list, name='index')
    # path("<str:name>", views.greet, name="greet")
]