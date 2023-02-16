from django.urls import path
from .views import reservation_list, reservation_detail, reservation_create
from .views import reservation_update, reservation_delete
urlpatterns = [
    path('', reservation_list, name='reservation_list'),
    path('<int:pk>/', reservation_detail, name='reservation_detail'),
    path('create/', reservation_create, name='reservation_create'),
    path('<int:pk>/update/', reservation_update, name='reservation_update'),
    path('<int:pk>/delete/', reservation_delete, name='reservation_delete'),
]
