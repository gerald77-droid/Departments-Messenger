from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
	path('home/',views.home ,name="home"),
	path('signin/', views.signin, name='signin'),
    path('signout/<int:pk>/', auth_views.LogoutView.as_view(), name='signout'),
	path('departments', views.department_view, name="departments"),
	path('signin',views.signin,name="signin"),
	path('profile-view/<int:pk>/',views.profile_view,name='profile-view'),
	path('profile',views.create_profile,name='profile'),
	path('department-details/<int:pk>/', views.department_details, name="department-details"),
	path('create-message/<int:pk>/', views.create_message, name="create-message"),
	path('message-details/<int:pk>/', views.message_details, name='message-details'),
	path('all-departments',views.all_departments,name='all-departments'),
	path('Navigation', views.Navigation, name="Navigation"),
	path('register-page', views.registerPage, name="register-page"),
	path('all-messages',views.all_messages,name='all-messages'),
	path('update-profile',views.update_profile,name='update-profile')
]

