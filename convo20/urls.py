from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^play/', views.PlayView.as_view(), name='play'),
    url(r'^stop/', views.StopView.as_view(), name='stop'),
    url(r'^update/', views.UpdateView.as_view(), name='update'),
]