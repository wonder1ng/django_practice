from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from accountapp.models import HelloWorld

# Create your views here.
# def hello_world(request):
#     return HttpResponse('Hello world!')

# def hello_world(request):
#     return render(request, 'base.html')

# def hello_world(request):
#     return render(request, 'accountapp/hello_world.html')

def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()	# 모델에서 테이블 인스턴스 변수 선언
        new_hello_world.text = temp     # text column에 temp 입력
        new_hello_world.save()          # 모델에 해당 record 저장

        # hello_world_list = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        return HttpResponseRedirect(reverse('accountapp:hello'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})