from django.urls import path
from royhat import views
urlpatterns = [
    path('', views.first_page, name='first_page'),
    path('post_jonatish/', views.post_jonatish, name='post_jonatish'),
    path('addAuto/', views.addAuto, name='addAuto'),
    path('edit_auto/<int:id>/', views.edit_auto, name='edit_auto'),
    path('delate_auto/<int:id>/', views.delate_auto, name='delate_auto')
]