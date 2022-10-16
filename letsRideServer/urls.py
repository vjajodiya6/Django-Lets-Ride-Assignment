from django.urls import re_path
from django.urls import path
from letsRideServer import views

urlpatterns=[
    re_path(r'request$',views.RequestsApi),
    re_path(r'request/([a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+)$',views.RequestsApi),
    re_path(r'rider$',views.RiderApi),
    re_path(r'rider/([a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+)$',views.RiderApi),
    re_path(r'matcher$',views.matcher),
    re_path(r'matcher/([a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+)$',views.matcher),
]
