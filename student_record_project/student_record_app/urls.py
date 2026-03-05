# from django.urls import path
# from .views import student_record_app, home
# from . import views

# urlpatterns = [
#     path('student_record_app/', student_record_app, name='student_record_app'),
#     path('', home, name='home'),
#     path('', views.student_list, name='student_list'),
#     path('create/', views.student_create, name='student_create'),
#     path('update/<int:pk>/', views.student_update, name='student_update'),
#     path('delete/<int:pk>/', views.student_delete, name='student_delete'),
# ]

from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.student_list, name='student_list'),   # Homepage shows list
#     path('create/', views.student_create, name='student_create'),
#     path('update/<int:pk>/', views.student_update, name='student_update'),
#     path('delete/<int:pk>/', views.student_delete, name='student_delete'),
# ]

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
