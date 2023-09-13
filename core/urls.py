
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
from authentication.serializers import *
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
 path('projects', views.ProjectList.as_view(), name='project-list'),
 path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='projectview'),
 path('requests', views.RequestList.as_view(), name='projectslistview'),
 path('requests/<int:pk>', views.RequestDetailView.as_view(), name='projectview'),
 path('bids/', views.BidProjectList.as_view(), name='bidproject-list'),
 path('stores/', views.StoreList.as_view(), name='store-list'),
 path('stores/<int:pk>', views.StoreDetailView.as_view(), name='storeview'),
 path('apply/', views.SupplierApplicationView.as_view(), name='supplier_application'),
 path('supplies/<int:pk>', views.SupplierDetailView.as_view(), name='supplierview'),
]