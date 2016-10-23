#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from .models import myUser


class SignupForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Email 주소를 입력해주세요.',
				'required': 'True',
			}),
		error_messages={'invalid':'Email 주소를 정확히 입력해주세요.'}
	)

	phone = forms.DecimalField(
		required=True,
		widget=forms.NumberInput(
			attrs={
				'class': 'form-control',
				'placeholder': '전화번호를 입력해주세요. (숫자만 입력)',
				'required': 'True',
			}
		)
	)

	password1 = forms.CharField(
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': '패스워드를 입력해주세요.',
				'required': 'True',
			}
		)
	)

	password2 = forms.CharField(
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': '패스워드를 다시한번 입력해주세요.',
				'required': 'True',
			}
		)
	)

	error_messages = {
		'password_mismatch':("패스워드가 일치하지 않습니다."),
	}

	class Meta:
		model = myUser
		fields = ('email', 'phone', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data['email']
		if myUser.objects.filter(email=email).exists():
			raise forms.ValidationError("존재하는 이메일 입니다.")
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


class LoginForm(AuthenticationForm):
	username = forms.EmailField(
		required=True,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': '로그인할 Email 주소를 입력해주세요.',
				'required': 'True',
			}),
		error_messages={'invalid':'Email 주소를 정확히 입력해주세요.'}
	)

	password = forms.CharField(
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'class': 'form-control',
				'placeholder': '패스워드를 입력해주세요.',
				'required': 'True',
			}
		)
	)

	# error_messages = {
 #        'invalid_login': (
 #            "Please enter a correct %(username)s and password. Note that both "
 #            "fields may be case-sensitive."
 #        ),
 #        'inactive': ("This account is inactive."),
 #    }

 #    def confirm_login_allowed(self, user):
	# 	if not user.is_active or not user.is_validated:
	# 		raise forms.ValidationError('no login', code='invalid_login')


	# def clean(self):
	# 	email = self.cleaned_data.get('email')
	# 	password = self.cleaned_data.get('password')

	# 	if email is not None and password:
	# 		self.user_cache = authenticate(self.request, email=email, password=password)
	# 		if self.user_cache is None:
	# 			raise forms.ValidationError(
	# 				self.error_messages['invalid_login'],
	# 				code='invalid_login',
	# 				params={'email': self.email_field.verbose_name},
	# 			)
	# 		else:
	# 			self.confirm_login_allowed(self.user_cache)

	# 	return self.cleaned_data
	# def save(self, commit=True):
	# 	user = super(UserCreationForm, self).save(commit=False)
	# 	user.set_password(self.cleaned_data["password1"])
	# 	if commit:
	# 		user.save()
	# 	return user

# class ProfileForm(forms.ModelForm):
# 	phone = forms.CharField(
# 		max_length=30,
# 		required=True,
# 		widget=forms.TextInput(
# 			attrs={
# 				'class': 'form-control',
# 				'placeholder': '전화번호를 입력해주세요.',
# 				'required': 'True',
# 			}
# 		)
# 	)

# 	company = forms.CharField(
# 		max_length=30,
# 		required=True,
# 		widget=forms.TextInput(
# 			attrs={
# 				'class': 'form-control',
# 				'placeholder': '회사명을 입력해주세요.',
# 				'required': 'True',
# 			}
# 		)
# 	)

# 	class Meta:
# 		model = Profile
# 		fields = ('phone', 'company')

