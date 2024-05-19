from django.urls import path
from . import views



urlpatterns = [
    path('', views.SacrecideHome.as_view(), name='home'),
    path('about/', views.Sacrecideabout.as_view(), name='about'),# http://127.0.0.1:8000
    path('past/', views.Sacrecidepast.as_view(), name='past'),  # http://127.0.0.1:8000
    path('merch/', views.Sacrecidemerch.as_view(), name='merch'),  # http://127.0.0.1:8000
    path('buy/<int:id_product>/', views.Sacrecidebuy.as_view(), name='buy'),  # http://127.0.0.1:8000
    path('send/', views.send_email, name='send'),  # http://127.0.0.1:8000
   #рабочая path('buy/<int:id_product>/', views.Sacrecidebuy.as_view(), name='buy'),  # http://127.0.0.1:8000

]
