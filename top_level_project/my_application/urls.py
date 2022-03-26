from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('slide/<int:slide_id>/', views.slide_page, name='slide')
]
