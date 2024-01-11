from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import password_validation



class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = ''
        
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control px-3 py-2','placeholder':'Password'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control px-3 py-2','placeholder':'Confirm Password'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'autofocus': True,'class':'form-control px-3 py-2','placeholder':'Email Address'}))
    class Meta:
        model = User
        fields = ['email','password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
        

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='',max_length=254, widget=forms.EmailInput(attrs={'autofocus': True,'placeholder':'Email Address','class':'form-control px-3 py-2'}))
    password = forms.CharField(label='',max_length=254, widget=forms.PasswordInput(attrs={'autofocus': True,'placeholder':'Password','class':'form-control px-3 py-2'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = User.objects.filter(email=username).first()
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data



class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=(""), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control px-3 py-2','autocomplete':'current-password','autofocus':True,'placeholder':'Old Password'}))
    new_password1 = forms.CharField(label=(""),strip=False,widget=forms.PasswordInput({'class':'form-control px-3 py-2','autocomplete':'new-password','placeholder':'New Password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=(""),strip=False,widget=forms.PasswordInput({'class':'form-control px-3 py-2','autocomplete':'new-password','placeholder':'Confirm New Password'}))
    
    
class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label='',max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control px-3 py-2','placeholder':'Email Address'}))
    
    
class SetMyPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))