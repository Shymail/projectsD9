from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, NewsList, NewsDetail, NewCreate, NewUpdate, NewDelete, upgrade_me, profile, AppointmentView, subscribe, unsubscribe, CategoryListView

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   # Отображение всех новостей и статей, где 'new_list' это класс во views
   path('post/', NewsList.as_view(), name='new_list'),
   #path('post/<int:pk>', NewsDetail.as_view()),

   # просмотр статей и новостей подробно по id(где 'post/<int:pk>' это 'post/1 или 2 или 3 ...')
   path('post/<int:pk>', NewsDetail.as_view(), name='new_detail'),

   # для создания новости через форму Новость
   path('post/new/create/', NewCreate.as_view(), name='new_create'),

   # для создания Статьи через форму Новость
   path('post/article/create/', NewCreate.as_view(), name='new_create'),

   # форма для обновления(добавление) Новости
   path('post/new/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),

   # форма для обновления(добавление) Статьи
   path('post/article/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),

   # форма для удаления Новости
   path('post/new/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),

   # форма для удаления Статьи
   path('post/article/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),

   # форма для шаблона стать автором
   path('upgrade/', upgrade_me, name='upgrade'),

   # путь формы для профиля
   path('profile/', profile, name='profile'),

   # Для записи человека куда либо
   path('appointment/', AppointmentView.as_view(), name='appointments'),

   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),

   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),

   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]