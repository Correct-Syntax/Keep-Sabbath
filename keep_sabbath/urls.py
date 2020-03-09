from django.conf.urls import url

from . import views 

app_name = 'keep_sabbath'

urlpatterns = [
    url(r'^$', views.keep_sabbath_page_view, name='sabbath-redirect'),
]