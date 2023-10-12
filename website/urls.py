from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home'),
    path("logout/",views.log_out,name='logout'),
    path("register/",views.register,name='register'),
    #查看单一数据信息
    path("records/<int:pk>",views.view_records,name='records'),
    #删除
    path("delete_record/<int:pk>",views.delete_record,name='delete_record'),
    path("update_record/<int:pk>",views.update_record,name='update_record'),
    path("add_record/",views.add_record,name='add_record')

]