from django.urls import path

from hello import views

urlpatterns = [
    path('', views.index, name='index'),
    path('required/', views.required, name='required'),
]
