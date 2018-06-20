from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^play/', views.PlayView.as_view(), name='play'),
    url(r'^stop/', views.StopView.as_view(), name='stop'),
    url(r'^update/', views.UpdateView.as_view(), name='update'),
    url(r'^student/', views.StudentView.as_view(), name='student'),
    url(r'^VIP/', views.VIP_View.as_view(), name='VIP'),
    url(r'^medal/', views.MedalView.as_view(), name='medal'),
    url(r'^index/', views.IndexView.as_view(), name='index'),
]