from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth .decorators import login_required
from django.http import HttpResponseNotFound

#from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from  .models import Role, Department, Message,UserProfile
from .forms import CustomUserForm,CreateUserForm

# Create your views here.
def home(request):
	return render(request,'base/home.html')



def registerPage(request):
	form=CreateUserForm()
	if request.method=="POST":
		form=CreateUserForm(request.POST)
		if form.is_valid:
			user=form.save(commit=False)
			user.username=user.username.lower()
			user.save()
			login(request,user)
			return redirect('home')
		else:
			messages.error(request,'An error occurred during registration')
	return render(request,'base/registration.html',{'form': form} )		



def Navigation(request):
	if request.user.is_authenticated:
		user_info={
			'username':request.user.name,
			'email':request.user.email,
			
		

		}
		
		context={'user_info':user_info}
		return render(request,'base/Navigation.html',context)
	else:
		return render(request,'base/signin.html')


def department_view(request):
	roles=Role.objects.all()
	user=get_user_model()
	admin_users=user.objects.filter(is_staff=True)
	
	if request.method=="POST":
		role_id=request.POST.get('role')
		dept_leader_id=request.POST.get('dept_leader')
		
		description=request.POST.get('description')
		role=Role.objects.get(id=role_id)
		dept_leader=user.objects.get(id=dept_leader_id)
		

	
		department=Department.objects.create(
			dept_leader=dept_leader,role=role,
			description=description
		)

		
		return redirect('Sucess Page')
	context={'roles':roles,'user_is_staff':request.user.is_staff}
	return render(request,'base/department.html', context)


def signin(request):
	if request.method=="POST":
		name=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=name,password=password)
		

		if user is not None:
			login(request,user)
			return redirect('Navigation')
			
		else:
			return render(request,'base/signin.html',{'error_message':'Invalid credentials'})
	context={}	
	return render(request,'base/signin.html',context)
@login_required
def profile_view(request,pk):
	User=get_user_model()
	user=User.objects.filter(id=pk).first()
	user_profile=UserProfile.objects.get(user=user)
	if user_profile is not None:
		user_departments=Department.objects.filter(members=user)
		user_messages=user.message_set.all()
		roles=Role.objects.all()
		context={'user':user,'user_profile':user_profile,'user_departments':user_departments,'user_messages':user_messages,'roles':roles}
		return render(request,'base/profile_view.html', context)
	else:
		return HttpResponseNotFound('user not found')

@login_required
def create_profile(request):
	form=CustomUserForm()
	if request.method=="POST":
		form=CustomUserForm(request.POST,request.FILES )
		if form.is_valid():
			form.save()
			messages.success(request,'user profile created successfully!')
			return redirect('profile-view')
		else:
			messages.error(request,'Error creating user profile.Please check the form ')
	context={'form':form}	
	return render(request,'base/profile.html',context)
@login_required
def update_profile(request):
	user=request.user
	form=CustomUserForm(instance=user)
	if request.method=="POST":
		form=CustomUserForm(request.POST,request.FILES,instance=user)
		if form.is_valid():
			form.save()
			messages.success(request,'User Profile updated successfully')
			return redirect('profile-view',pk=user.id)
		else:
			messages.error(request,'Error updating the profile picture')
	context={'user':user,'form':form}
	return render(request,'base/update_profile.html',context)	




def department_details(request,pk):
	department=Department.objects.get(id=pk)
	department_messages=department.message_set.all()
	department_members=department.members.all()
	if request.method=="POST":
		title=request.POST.get('Title')
		content=request.POST.get('content')
		message=Message.objects.create (
			user=request.user,
			department=department,
			Title=title,
			content=content
			
			)
		department.members.add(request.user)
		return render(request,'base/department_details.html')

	context={ 'department':department,'department_messages':department_messages,'department_members':department_members}
	return render(request, 'base/department_details.html', context)
@login_required
def create_message(request,pk):
	user=get_user_model().objects.get(id=pk)
	departments=Department.objects.all()
	if request.method=="POST":
		message_title=request.POST.get('title')
		department=request.POST.get('department')
		message_content=request.POST.get('content')
		Message.objects.create(
		user=user, message_title=message_title, message_content=message_content,department=department
	)
		return redirect('message-details',pk=request.user.id)
	context={'user':user,'departments':departments}
	return render(request,'base/create-message.html',context)

def message_details(request,pk):
	User=get_user_model()
	user=User.objects.get(id=pk)
	user_messages=Message.objects.filter(user=user)
	context={'user':user,'user_messages':user_messages}
	return render(request,'base/message_detail.html',context)

def all_departments(request):
	q=request.GET.get('q') if request.GET.get('q')!=None else ''
	departments=Department.objects.filter(name__icontains=q)
	return render(request,'base/all_department.html',{'departments':departments})
def all_messages(request):
	department_messages=Message.objects.all()
	context={'department_messages':department_messages}
	return render(request,'base/all_messages.html',context)

@login_required
def signout(request,pk):
	User=get_user_model
	user=User.objects.get(id=pk)
	logout(request,user)
	return redirect('home')


				

		
