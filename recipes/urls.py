from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:category_val>', views.category, name='category'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
]