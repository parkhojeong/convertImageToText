from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
import googleAPI

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'msg':'need to upload image'})

    elif request.method == "POST":
        res = googleAPI.orc_kor_eng(request.FILES['image'].file)
        res = res.split('\n')
        res = res[:len(res) // 2]
        return render(request,'index.html',{'msg': res})