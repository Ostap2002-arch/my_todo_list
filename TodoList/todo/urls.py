from django.urls import path

from . import views

urlpatterns = [
    path('todo', views.new_page, name = 'index'),
    path('create_categories', views.create_categories, name = 'create_categories' ),
    path('show_all_categories', views.show_all_categories, name = 'show_all_categories'),
    path('create_and_show_tasks/<slug:name_category>', views.create_and_show_tasks, name = 'create_and_show_tasks'),
]