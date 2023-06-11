from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout


def user_login(request):
	if request.method == 'POST':

		email = request.POST["email"]
		password = request.POST["password"]

		user = authenticate(request, email=email, password=password)

		if user is not None:
			# User credentials are correct, log in the user
			login(request, user)
			# Redirect to a success page or any other desired page
			return redirect('index')
		else:
			error_message = 'メールアドレスか、パスワードが間違っています。'
			return render(request, 'users/login.html', {'error_message': error_message})
	else:
		if request.user.is_authenticated:
			return redirect('index')

		return render(request, 'users/login.html')


def user_logout(request):
	logout(request)
	return redirect('login')
