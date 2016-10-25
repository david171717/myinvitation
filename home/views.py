from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import SignupForm, LoginForm
# from .forms import SignupForm, LoginForm, ProfileForm
from .models import myUser
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import password_validation
from django.db import transaction



def index(request):
	return render(request, 'home/index.html', {})

def signup(request):
	if request.method == "POST":
		signupform = SignupForm(request.POST)
		# profileform = ProfileForm(request.POST)
		if signupform.is_valid():
		# if signupform.is_valid() and profileform.is_valid():
			user = signupform.save(commit=False)
			# password_v = password_validation.validate_password(user.password)
			# if password_v is not None:
			# 	return HttpResponseRedirect(reverse("/"))
			# user = profileform.save()
			# user.email = signupform.cleaned_data['email']
			# user.set_password(user.password)
			user.save()

			return HttpResponseRedirect(reverse("signup_ok"))
	else:
		signupform = SignupForm()
		# profileform = ProfileForm()
	return render(request, 'home/signup.html', {'signupform': signupform})
	# return render(request, 'home/signup.html', {'signupform': signupform, 'profileform':profileform})

def signup_ok(request):
	return render(request, 'home/signup_ok.html', {})


# def loginview(request):
# 	email = password = ''
# 	if request.method == "POST":
# 		# global loginform
# 		# global email
# 		# email = request.POST['email']
# 		# password = request.POST['password']
# 		email = request.POST.get('email', False)
# 		password = request.POST.get('password', False)

# 		user = authenticate(email=email, password=password)

# 		if user is not None:
# 			if user.is_active:
# 				login(request, user)
# 				return HttpResponseRedirect(reverse("index"))
# 		# else:
# 		# 	clean(self)
# 			# loginform = LoginForm()
# 			# return HttpResponseRedirect(reverse("index"))
# 			# raise request.ValidationError('nono')

# 	else:
# 		loginform = LoginForm()
# 	# global loginform
# 	return render(request, 'home/login.html', {'loginform': loginform})
# 	# return render_to_response('home/login.html', context=RequestContext(request))

# def logoutview(request):
# 	logout(request)
# 	return render(request, 'home/index.html', {})
def introduction(request):
	return render(request, 'home/introduction.html', {})

def application(request):
	return render(request, 'home/application.html', {})	

def invitation(request):
	return render(request, 'home/invitation.html', {})

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = SignupForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = SignupForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

# def set_password(self, raw_password):
#         # whatever logic you need to set the password for your user or maybe
# 		self.user.set_password(raw_password)
# def clean_password2(self):
# 	password1 = self.cleaned_data.get("password1")
# 	password2 = self.cleaned_data.get("password2")
# 	if password1 and password2 and password1 != password2:
# 		raise forms.ValidationError(
# 			self.error_messages['password_mismatch'],
# 			code='password_mismatch',
# 		)
# 	return password2




# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})