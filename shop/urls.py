from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('reviews/', views.reviews, name='reviews'),
    path('display_reviews/', views.display_reviews, name='display_reviews'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]