from django.urls import path, re_path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, "year4")


urlpatterns = [
    path('', views.index, name='about'),
    path('about/', views.about, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]