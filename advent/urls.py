from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.DateList.as_view(), name='date_list'),
    path('<month>/<day>/', views.DateDetail.as_view(), name='date_detail'),
]