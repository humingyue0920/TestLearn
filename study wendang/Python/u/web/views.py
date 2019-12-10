from django.shortcuts import render
import json
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
# Create your views here.


def Login(request):
    if request.method == 'POST':
        result = {}
        user_name = request.POST.get('username')
        key = request.POST.get('password')
        result['user_name'] = user_name
        result['key'] = key
        result['status_code'] = '200'
        result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
        # return json.dumps(result, ensure_ascii=False, indent=2)
    else:
        return render_to_response('login.html')


def LoginOut(request):
    if request.method == 'GET':
        result = {}
        user_name = request.GET.get('username')
        key = request.GET.get('password')
        result['user_name'] = user_name
        result['key'] = key
        result['status_code'] = '200'
        result = json.dumps(result, ensure_ascii=False, indent=2)
        return HttpResponse(result, content_type='application/json;charset=utf-8')



