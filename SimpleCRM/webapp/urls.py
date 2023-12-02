from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""), # homepage
    
    path('register', views.register, name="register"), # register new user

    path('my-login', views.my_login, name="my-login"), # login user
    
    path('user-logout', views.user_logout, name="user-logout"), # logout user

    # CRUD bellow

    path('dashboard', views.dashboard, name="dashboard"), # read records
    
    path('create-record', views.create_record, name="create-record"), # create record

    path('update-record/<int:pk>', views.update_record, name="update-record"), # update record

    path('record/<int:pk>', views.singular_record, name="record"), # view single record

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"), # delete record
    
]
