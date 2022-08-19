from django.urls import path
from .import views as v

urlpatterns = [
    
    path("", v.index, name="task"),
    path('result',v.result,name='result'),
    
]