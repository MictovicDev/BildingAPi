
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from . import views
from authentication.serializers import *
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
 path('projects', views.ProjectGetCreate.as_view(), name='project'),#list and create projects
 path('projects/user', views.UserProject.as_view(), name='project'),#get a projectdetail
 path('projects/<int:pk>', views.GetUpdateDelProject.as_view(), name='projecttdetail'),
 path('recentprojects', views.RecentProjectView.as_view(), name='recentprojects'),#list and create projects
 path('recentprojects/<str:pk>', views.RecentProjectDetailView.as_view(), name='recentproject-detail'),#get a projectdetail
 path('requests', views.RequestView.as_view(), name='projectslistview'),
 path('requests/user', views.UserRequest.as_view(), name='usersrequest'),
 path('requests/<int:pk>', views.GetUpdateDelRequest.as_view(), name='requestdetail'),
 path('bids/', views.BidProjectList.as_view(), name='bidproject-list'),
 path('bids/user/', views.ContractorProjectApplications.as_view(), name='bidproject-list'),
 path('bids/user/<int:pk>', views.GetProject.as_view(), name='bidproject-list'),
 path('applies/', views.ApplyRequestList.as_view(), name='bidproject-list'),
 path('applies/<int:pk>', views.CreateApplicationView.as_view(), name='bidproject-create'),
 path('bids/update/<int:pk>', views.BidUpdateView.as_view(), name='hire'),
 path('bids/<int:pk>', views.CreateBidView.as_view(), name='bidproject-create'),
 path('bids/all/', views.ListBidView.as_view(), name='listbid'),
 path('bids/accept/<int:pk>', views.AcceptBidView.as_view(), name='acceptbid'),
 path('stores/', views.StoresView.as_view(), name='store-list'),
 path('items/', views.ItemList.as_view(), name='item'),
 path('items/<str:pk>', views.ListItem.as_view(), name='item-list'),
 path('users/applications', views.UsersApplications.as_view(), name='users_applications'),
 path('reviews/<str:pk>', views.ReviewsView.as_view(), name='reviews'),
 path('hired/count', views.HiredCount.as_view(), name='hiredcounts')

]