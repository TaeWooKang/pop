from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Member
from django.utils import timezone
# Create your views here.

def main(request):
    return render(request,'homepage/main.html',{})


def join_agree(request):
    return render(request,'homepage/join_agree.html',{})



def join(request):
    if request.method=='GET':
        return render(request, 'homepage/join.html', {})
    else:
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']
        user_name = request.POST['user_nick']
        user_email = request.POST['user_email']

        member = Member(user_id=user_id,
                        user_pwd=user_pwd,
                        user_nick=user_name,
                        user_email=user_email)
        member.c_date = timezone.now()
        member.save()

        return HttpResponse('가입완료')



def ID_check(request):
    user_id = request.POST['user_id']
    try:
        Member.objects.get(user_id=user_id)
    except Member.DoesNotExist as e:
        pass
        res = {'user_id': user_id, 'msg': '가입 가능'}
        return JsonResponse(res)
    else:
        res = {'user_id': user_id, 'msg': '가입 불가'}
        return JsonResponse(res)

def nick_check(request):
    user_nick = request.POST['user_nick']
    try:
        Member.objects.get(user_nick=user_nick)
    except Member.DoesNotExist as e:
        pass
        res = {'user_nick': user_nick, 'msg': '가입 가능'}
        return JsonResponse(res)
    else:
        res = {'user_nick': user_nick, 'msg': '가입 불가'}
        return JsonResponse(res)







def login(request):
    result = ''
    if request.method=='GET':
        return render(request, 'homepage/login.html', {})
    else:
        user_id = request.POST['user_id']
        user_pwd = request.POST['user_pwd']

        try:
            Member.objects.get(user_id = user_id,
                           user_pwd = user_pwd)
        except Member.DoesNotExist:
            return HttpResponse('로그인 실패')
        return HttpResponse('로그인 완료')
