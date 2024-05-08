from django.urls import path, re_path
from schedulerCrud import views
from django.contrib import admin

# urls.py
urlpatterns = [
    path('Home/GetData', views.GetData),
    path('Home/UpdateData/', views.UpdateData),
    path('admin/', admin.site.urls),
]