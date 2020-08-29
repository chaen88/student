from django.contrib import admin
from django.urls import path
from main.views import index, detail, update, create, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('detail/<int:student_id>',detail,name="detail"),
    path('update/<int:student_id>',update,name="update"),
    path('create/',create,name='create'),
    path('delete/<int:student_id>',delete,name="delete"),
    
]