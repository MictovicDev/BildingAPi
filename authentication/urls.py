
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
    path('auth/changepassword', views.ChangePasswordView.as_view(), name='changepassword'),
    # path('auth/login', views.UserLoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #refresh token
    path('auth/contractor/', views.ContractorCreateView.as_view(), name='contractor_signup'),#contractorsignup
    path('auth/update/', views.UsersUpdateView.as_view(), name='updateuserwithid'),
    path('auth/update/<str:pk>', views.MyUsersUpdateView.as_view(), name='updateuserwitoutid'),
    path('auth/supplier/', views.SupplierListCreateView.as_view(), name='supplier_signup'), #suppliersignup
    path('auth/worker/', views.WorkerListCreateView.as_view(), name='worker_signup'),#workersignup
    path('users/', views.UsersListView.as_view(), name='listusers'),#listallusersinthedatabase
    path('auth/edit', views.EditProfileView.as_view(), name='editprofile'),
    path('auth/activation/<str:token>', views.ActivateAccount.as_view(), name='activateaccount'),#activateuseraccount
    path('accounts/', views.SocialAuthentication.as_view(), name='socialauth') #social authentication
]

