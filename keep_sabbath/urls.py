from django.urls import re_path

from . import views 

app_name = 'keep_sabbath'

urlpatterns = [
    re_path(r'^$', views.keep_sabbath_page_view, name='sabbath-redirect'),
]