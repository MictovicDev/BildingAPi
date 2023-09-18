
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView
from authentication.serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'), #you can use to login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #refresh token
    path('auth/contractor/', views.ContractorCreateView.as_view(), name='contractor_signup'),#contractorsignup
    path('auth/update/<str:pk>', views.UsersUpdateView.as_view(), name='contractordetails'),
    path('auth/supplier/', views.SupplierCreateView.as_view(), name='supplier_signup'), #suppliersignup
    path('auth/worker/', views.WorkerCreateView.as_view(), name='worker_signup'), #workersignup
    path('auth/activation/<str:token>', views.ActivateAccount.as_view(), name='activateaccount') #activateuseraccount
]


