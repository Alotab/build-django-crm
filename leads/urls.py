
from django.urls import path
from . import views

# app_name="leads"

urlpatterns = [
    path('', views.lead_list, name='home'),
    path('create/', views.lead_create, name='create'),
    path('<int:pk>/update/', views.lead_update, name='update'),
    path('detail/<int:pk>', views.lead_detail, name='detail'),
    path('<int:pk>/delete/', views.lead_delete, name='delete'),
]