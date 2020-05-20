#from django.shortcuts import render,redirect
#from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
#we use this form which are provided by django so we do not need to validation manually
#we can create python class togenerate html form and some class are provided by django here UserCreaitionForm class for form
#message.debug,message.info,message.success,message.warning,message.error


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
def friend(request,id):
    Cuser=request.user;
    print(Cuser)
    users=User.objects.all()
    for user in users:
        if user.id==id:
            Cuser.profile.friends=" "+user.username;
            user.profile.friends=Cuser;
            friend1=Cuser.profile.friends;
            friend2=user.profile.friends;
            print(user.profile.friends)
            #print(Cuser.profile.friends)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            # p_form2=ProfileUpdateForm(request.POST,instance=Cuser.profile)
            # p_form.save()
            # p_form2.save()
            context = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'mobile_no': user.profile.mobile_no,
                'clg_name': user.profile.clg_name,
                'degree': user.profile.degree,
                'skill': user.profile.skill,
                'jobs': user.profile.jobs,
                'image': user.profile.image,
                'friends':user.profile.friends,
                'msg': "request send",
            }
    return render(request, 'users/profile1.html',context)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
def profile1(request,id):
    print("profile")
    user1=id
    #print(user1)
    users=User.objects.all()
    u_form=[]
    p_form=[]
    context={}
    for user in users:
        if user.id==user1:
            #print(user)
            #print(user.profile)
            context={
            'id':user.id,
            'username':user.username,
            'email':user.email,
            'mobile_no':user.profile.mobile_no,
            'clg_name':user.profile.clg_name,
            'degree':user.profile.degree,
            'skill':user.profile.skill,
            'jobs':user.profile.jobs,
            'image':user.profile.image,
            'msg':"friend",
            }
            break;
    return render(request, 'users/profile1.html', context)
# we use this decorator so we use profile url if and only if we have logged in.
# if we do not use decorator then we can accest profile page with manully write profile url in ulr bar without logged in
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        #which is uploaded bu user from his/her p.c.'s location
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        #which is uploaded bu user from his/her p.c.'s location
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/edit.html', context)