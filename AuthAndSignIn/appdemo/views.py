from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from appdemo import models
import datetime
import json

# Create your views here.

class Auth(object):
    # 用于认证的类
    def dispatch(self,request,*args,**kwargs):
        if not request.session.get('userinfo'):
            return redirect('/login')
        res = super(Auth,self).dispatch(request, *args, **kwargs)
        return res

class Login(View):
    # 登录视图
    def get(self,request,*args,**kwargs):
        return render(request, 'login.html')
    def post(self,request,*args,**kwargs):
        user = request.POST.get('user')
        password = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(user=user,password=password).first()
        if user_obj:
            request.session['userinfo'] = user
            return redirect('/sign/')
        return render(request, 'login.html')

class Sign(Auth,View):
    # 签到视图,必须登录才能签到
    def get(self,request,*args,**kwargs):
        content = {'userinfo':request.session.get('userinfo')}
        return render(request, 'sign.html', content)
    def post(self,request,*args,**kwargs):
        data = {'status_code':10000,'msg':None}
        current_date = datetime.date.today()
        user = request.POST.get('user')
        sign_obj = models.Sign.objects.filter(user__user=user,sign_date__date=current_date).first()
        if sign_obj:
            data['status_code'] = 10001
            data['msg'] = '对不起，你今日已签到，不能重复签到'
        else:
            user_obj = models.UserInfo.objects.filter(user=user).first()
            models.Sign.objects.create(user=user_obj)
            data['msg'] = '今日签到成功'
        return HttpResponse(json.dumps(data))

class Logout(View):
    # 注销视图
    def get(self,request,*args,**kwargs):
        request.session['userinfo'] = None
        return redirect('/login/')
