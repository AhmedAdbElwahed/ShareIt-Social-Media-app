from django.urls import path, include
# from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # Login and Logout
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # # Password Change
    # path('password-changed/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # # Password Reset
    # path('password-reset/',
    #      auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-rest-done',
    #      auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/',
    #      auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # The default authentication urls introduced by django
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit_profile, name='edit'),
    path('users/', views.user_list, name='user_list'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/<str:username>/', views.user_detail, name='user_detail'),
]
