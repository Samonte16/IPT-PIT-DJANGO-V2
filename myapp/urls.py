from django.urls import path
from .views import (
    signup_view, signin_view, verify_email,
    admin_register_view, admin_login_view, verified_users_view,
    forgot_password_view, admin_verify_email, admin_forgot_password_view
)

urlpatterns = [
    path('api/signup/', signup_view, name='signup'),
    path('api/signin/', signin_view, name='signin'),
    path('api/verify-email/<uuid:token>/', verify_email, name='verify_email'),
    path('api/admin-verify-email/<uuid:token>/', admin_verify_email, name='admin_verify_email'),
    path('api/admin/register/', admin_register_view, name='admin_register'),
    path('api/admin/login/', admin_login_view, name='admin_login'),
    path('api/admin/verified-users/', verified_users_view, name='verified_users'),
    path('api/forgot-password/', forgot_password_view, name='forgot_password'),
    path('api/admin-forgot-password/', admin_forgot_password_view, name='admin_forgot_password'),
]
