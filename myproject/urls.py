from django.contrib import admin
from django.urls import path
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name="index"),
    path('detail/<int:student_id>',main.views.detail,name="detail"),
    path('update/<int:student_id>',main.views.update,name="update"),
    path('create/<int:student_id>',main.views.create,name="create"),
    
]
