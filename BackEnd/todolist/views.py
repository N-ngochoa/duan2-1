from django.utils import timezone
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.http import Http404
from django.views import generic,View
from django.contrib.auth import authenticate,login,logout,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import nguoi_dung,to_do_list,item,to_do_share
from django.contrib.sessions.models import Session

def user_id_from_session():
    dict_session = Session.objects.all()[0].get_decoded()
    user = dict_session['_auth_user_id']
    return user
@decorators.login_required(login_url='/')
def index(request):
    user=user_id_from_session()
    to_do_list_user = to_do_list.objects.filter(user=user, is_public=False)
    to_do_list_public = to_do_list.objects.filter(is_public=True)
    to_do_list_shared = to_do_list.objects.filter(todoshare_todo__user=user)
    context = {'todolistuser' : to_do_list_user,
    'todolistpublic' : to_do_list_public,
    'todolistshared' : to_do_list_shared,
    'user' : user,
    }
    # response = response()
    return render(request, 'todolist/index.html', context)

@decorators.login_required(login_url='/')
def tododetail(request, todo_id):
    try:
        to_do = to_do_list.objects.get(pk=todo_id)
    except to_do_list.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'todolist/detail.html', {'todolist':to_do})

def logout_view(request):
    logout(request)
    return redirect('/')

def loginview(request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return render(request, 'todolist/login.html')

@decorators.login_required(login_url='/')
def create_todo(request):
    to_do_list.objects.create(name='to do list mới', date_create=timezone.now(), is_public=False, user=nguoi_dung.objects.get(id=user_id_from_session()))
    return redirect('/index')

@decorators.login_required(login_url='/')
def delete_todo(request, todo_id):
    to_do = to_do_list.objects.get(pk=todo_id)
    to_do.delete()
    return redirect('/index')

@decorators.login_required(login_url='/')
def update_todo(request, todo_id):
    print(todo_id)
    print(request.POST['todo_name'])
    print(request.POST['todo_ispublic'])
    to_do = to_do_list.objects.get(pk=todo_id)
    to_do.name = request.POST['todo_name']
    to_do.is_public = request.POST['todo_ispublic']
    to_do.save()
    return redirect('/index')

@decorators.login_required(login_url='/')
def create_item(request, todo_id):
    to_do = to_do_list.objects.get(pk=todo_id)
    item.objects.create(name='item mới', to_do=to_do)
    return redirect('/'+str(to_do.pk))

@decorators.login_required(login_url='/')
def delete_item(request, item_id, todo_id):
    items = item.objects.get(pk=item_id)
    items.delete()
    return redirect('/'+str(todo_id))

@decorators.login_required(login_url='/')
def update_item(request, item_id, todo_id):
    to_item = item.objects.get(pk=item_id)
    to_item.name = request.POST['item_name']
    to_item.save()
    return redirect('/'+str(todo_id))
# Create your views here.
