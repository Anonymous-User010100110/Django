



from django.urls import path

from . import views

from django,contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),

]
urlpatt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         erns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]