from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def post_home(request):
	home = 'This is home'
	return render_to_response('home.html',{'name':home})

def post_detail(request):
	return HttpResponse('<h1>Детали</h1>')

def post_update(request):
	return HttpResponse('<h1>Обновления</h1>')

def post_delete(request):
	return HttpResponse('<h1>Удаление</h1>')

def post_create(request):
	return HttpResponse('<h1>Создание</h1>')

def post_list(request):
	return HttpResponse('<h1>Лист</h1>')