from django.urls import path
from eMobilis_app import views




urlpatterns=[
    path('',views.home,name='eMobilis_home'),
    path('about',views.about,name='eMobilis_about'),
    path('contact',views.contact,name='eMobilis_contact'),
    path('blog',views.blog,name='eMobilis_blog'),
    path('services',views.services,name='eMobilis_services'),

]