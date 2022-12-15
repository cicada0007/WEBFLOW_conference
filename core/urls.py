from django.urls import * 
from . import views


urlpatterns =[
    path('about',views.about,name='about'),
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('courses',views.courses,name='courses'),
    path('teacher',views.teacher,name='teacher'),
    path('blog_single',views.blog_single,name='blog_single'),

]