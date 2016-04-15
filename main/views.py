from django.shortcuts import render, redirect
from main.models import Case, Update, Photo, CustomUser
from forms import SignUpForm, LoginForm, CreateCaseForm, CreateUpdateForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


# Create your views here.

# Create your views here.

#data managment views
def case_list(request):

	context = {}

	cases = Case.objects.filter(user=request.user.pk)

	context['cases'] = cases

	return render(request, 'case_list.html', context)

def create_case(request):

	context = {}

	context['form'] = CreateCaseForm()

	if request.method == 'POST':

		form = CreateCaseForm(request.POST)

		context['form'] = form

		if form.is_valid():

			case = form.save(commit=False)

			#user_obj = CustomUser.objects.get(pk=request.user.pk)

			case.user = request.user

			case.save()

			return redirect('/case_detail/%s' % case.pk)

	return render(request, 'create_case.html', context)


def case_detail(request, pk):

	case = Case.objects.get(pk=pk)

	context = {}

	context['case'] = case

	return render(request, 'case_detail.html', context)


#updates managment views

def create_update(request, pk):

	context = {}

	case = Case.objects.get(pk=pk)

	if request.user == case.user:

		form = CreateUpdateForm(initial={'date': datetime.now()})

		context['form'] = form
		context['case'] = case
		if request.method == 'POST':

			form = CreateUpdateForm(request.POST, request.FILES)

			context['form'] = form

			if form.is_valid():

				update = form.save(commit=False)

				update.case = case

				update.save()

				new_photo = Photo()

				print form.data 
				print form.cleaned_data

				new_photo.image = form.cleaned_data['image']

				new_photo.update = update

				new_photo.image_text = form.cleaned_data.get('image_text', None)

				new_photo.save()


				

				return redirect('/case_detail/%s' % case.pk)
	else:
		return HttpResponse('GO OUT YA SADEEQ !')
	
	
	print context
	return render(request, 'create_update.html', context)

def delete1(request, pk):
	case = Case.objects.get(pk=pk)
	if request.user == case.user:
		context = {}
		context['case'] = case
		return render(request, 'delete1.html', context)
	return redirect('/case_list/')

def delete2(request, pk):
	case = Case.objects.get(pk=pk)
	if request.user == case.user:
		case.delete()
	return redirect('/case_list/')

def deleteupdate1(request, pk):
	update = Update.objects.get(pk=pk)
	if request.user == update.case.user:
		context = {}
		context['update'] = update
		return render(request, 'deleteupdate1.html', context)
	return redirect('/case_list/')

def deleteupdate2(request, pk):
	update = Update.objects.get(pk=pk)
	if request.user == update.case.user:
		update.delete()
	return redirect('/case_detail/%s' % update.case.pk)


#user managment views
def logout_view(request):
	logout(request)
	return redirect('/signup/')

def login_view(request):

	context = {}

	context['form'] = LoginForm()

	if request.method == 'POST':

		form = LoginForm(request.POST)

		if form.is_valid():

			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password', None)

			auth_user = authenticate(username=email, password=password)

			try:
				login(request, auth_user)
				return redirect('/case_list/')
			except Exception, e:
				return HttpResponse('invalid user, try again <a htrf="/login/">here</a>')
	return render(request, 'login.html', context)

def signup(request):

	context = {}

	context['form'] = SignUpForm()

	if request.method == 'POST':

		form = SignUpForm(request.POST)

		context['form'] = form

		if form.is_valid():

			form.save()

			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password1', None)

			auth_user = authenticate(username=email, password=password)

			try:
				login(request, auth_user)
			except Exception, e:
				return HttpResponse('invalid user, try again <a htrf="/signup/">here</a>')

	return render(request, 'signup.html', context)











