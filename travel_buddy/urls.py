from django.urls import path
from . import views

urlpatterns = [
    path('', views.travels, name='travels'),
    path('add', views.add_travel, name='add_travel'),
    path('new_travel', views.new_travel, name='new_travel'),
    path('destination/<int:travel_id>', views.view_travel, name='view_travel'),
]