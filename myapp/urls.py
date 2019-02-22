from django.urls import path

from . import views

#app_name = "myapp"

urlpatterns = [
    #path('', views.index, name='index'),
    path('uploadfarmer/', views.upload1, name='upload1'),
    path('uploadvillage/', views.upload2, name='upload2'),
    path('uploadfarmer/excel_upload1', views.upload1, name='excel_upload1'),
    path('uploadvillage/excel_upload2', views.upload2, name='excel_upload2')

]