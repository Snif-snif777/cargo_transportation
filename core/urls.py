from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('service/', views.service, name='services'),
    path('about/', views.about, name='about'),
    path('service-details/', views.service_details, name='service_details'),
    path('elements/', views.elements, name='elements'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.single_blog, name='single_blog'),
    path('contact/', views.contact, name='contact'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),

]
