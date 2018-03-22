from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib import admin
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
# Create your views here.

__all__ = ('LoginView', 'LogoutView', 'ChangePassword',)


def LoginView(request):
    template_response = login(
        request,
        template_name='cost/indexhtml',
    )
    return template_response


def LogoutView(request):
    template_response = logout_then_login(
        request,
        login_url=  redirect('/cost/index') #reverse('login:login')
    )
    return template_response


# def ChangePassword(request):
#     template_response = password_change(request,
#                                         template_name='common/form.html',
#                                         password_change_form=PasswordChangeForm,
#                                         post_change_redirect=reverse('main:main'),
#                                         extra_context={'doc': '密码修改', })
#     return template_response


def index(request):
    return  render(request,'cost/login.html')

def userlogin(request):

    if request.method == "POST":
        request.session.set_expiry(0)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user :
            if user.is_active:
                auth.login(request, user)
                request.session['userId'] = user.id
                request.session['user']=username
                return redirect('/cost/listing')
        else:
            return redirect('/cost/login')
    return render(request, 'cost/login.html')

def userlogout(request):
    logout(request)
    request.session.flush()
    return redirect('/cost/index')


def listing(request):

    user = User.objects.get(pk =  request.session['userId'])
    contact_list = Recharge_and_cost.objects.filter(member= user)
    costsum = 0
    amountsum = 0
    for re in contact_list:
        if re.cost:
            costsum = costsum + re.cost
        else:
            costsum = costsum + 0
        if re.recharge:
            amountsum = amountsum+ re.recharge.recharge
        else:
            amountsum =amountsum+ 0
    paginator = Paginator(contact_list, 5,orphans=0,allow_empty_first_page = True)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    context = { 'contacts': contacts,'costsum':costsum,'amountsum':amountsum,'remainder':amountsum - costsum}
    return render(request, 'cost/index.html',  context)

class RecoreList(ListView):
    model=Recharge_and_cost
    template_name='cost/index.html'
    paginate_by = 1

    def get_queryset(self):
        qs=super(RecoreList,self).get_queryset()
        qs=qs.filter(member=self.request.user)
        return qs