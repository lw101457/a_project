import hashlib
import time

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import Lunbo, Mobile, Phone, User, Cart


# 主页
def index(request):
    mobile = Mobile.objects.all()
    phone = Phone.objects.all()
    lunbo = Lunbo.objects.all()
    username = request.session.get('username')
    users = User.objects.filter(username=username)
    if users:
        users = users[0]
    lunsli = lunbo[:4]
    lunder = lunbo[4:8]
    lunadd = lunbo[9:]
    lunboslider = {
        'phone': phone,
        'lunsli': lunsli,
        'lunder': lunder,
        'lunadd': lunadd,
        'mobile': mobile,
        'users': users,
    }

    return render(request, 'index.html', context=lunboslider)


# 详情页
def details(request, goodid):
    username = request.session.get('username')
    users = User.objects.filter(username=username)
    if users:
        users = users[0]
    mobile = Mobile.objects.get(id=goodid)
    return render(request, 'details.html', context={"mobile": mobile,'users':users})


def genetate_token():
    token = str(time.time())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()


# 注册
def registered(request):
    if request.method == 'GET':
        return render(request, 'registered.html')
    elif request.method == "POST":
        user = User()
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('pwd1')
        user.email = email
        user.username = username
        user.password = password

        user.token = genetate_token()
        user.save()
        # 状态保持
        response = redirect('app:index')
        # print("(能到这里嘛?")
        request.session['username'] = username

        return response


# 退出
def logout(request):
    rseponse = redirect('app:index')
    rseponse.delete_cookie('token')
    del request.session['username']
    return rseponse


#  登录
def login(request):
    if request.method == "GET":
        return render(request, 'registered.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).filter(password=password)
        if user.count():
            # 状态保持
            response = redirect('app:index')
            request.session['username'] = username
            return response
        else:
            return render(request, 'registered.html')


# 购物车
def cart(request):
    username = request.session.get('username')
    users = User.objects.filter(username=username)
    if users:
        users = users[0]
    carts = Cart.objects.all()
    print(carts)
    return render(request, 'cart.html',{'carts':carts,'users':users})


def addcart(request):
    token = request.session.get('username')
    print('添加购物车')
    print('token',token)
    user = User.objects.filter(username=token)[0]
    goodid = request.GET.get('goodid')
    good = Mobile.objects.get(pk=goodid)
    if token:
        # pass
        cart = Cart.objects.filter(user=user,goods=good)
        if cart:
            cart = cart[0]
            cart.number +=1
        else:
            cart = Cart()
            cart.user = user
            cart.goods = good
            cart.number = 1
        cart.save()
        return JsonResponse({'msg':'ok'})
    else:
        print(token)
        return redirect(reverse('app:registered'))

def addgood(request):
    cart = request.GET.get('cart')
    cart = Cart.objects.get(pk=cart)
    cart.number +=1
    cart.save()
    return JsonResponse({'msg':'ok'})

def delgood(request):
    cart = request.GET.get('cart')
    cart = Cart.objects.get(pk=cart)
    if cart.number==1:
        cart.delete()
        return redirect('app:cart')
    else:
        cart.number -= 1
        cart.save()
        return JsonResponse({'msg':'ok'})
