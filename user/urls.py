from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user.forms import ChangePasswordForm, ResetPasswordForm, SetMyPasswordForm

urlpatterns = [
    path('',views.UserRegistrationView.as_view(),name='signup'),
    path('signin/',views.signin,name='signin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',auth_views.LogoutView.as_view(next_page='signin'),name='logout'),
    path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='user/changepassword.html',form_class=ChangePasswordForm,success_url='/changepassworddone/'),name='changepassword'),
    path('changepassworddone/',auth_views.PasswordChangeView.as_view(template_name='user/changepassworddone.html'),name='changepassworddone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html',form_class=ResetPasswordForm),name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html',form_class=SetMyPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),
]
