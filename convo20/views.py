from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from convo20.models import Student
from convo20.scripts import caspar
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model, authenticate, login, logout
# from django.contrib import messages
# import datetime
# from django.db import IntegrityError

# Create your views here.

# Renders the main frontend page.
class IndexView(View):
	def get(self, request, *args, **kwargs):
		temp = list(Student.objects.all())
		all_programmes = set()
		all_branches = set()
		for i in temp:
			all_programmes.add(i.programme)
			all_branches.add(i.branch)
		context = {
			'all_programmes' : all_programmes,
			'all_branches' : all_branches,
		}
		return render(request, 'convo20/index.html', context)

class UpdateView(View):
	def post(self, request, *args, **kwargs):
		programme 	= request.POST.get('programme')
		branch 		= request.POST.get('branch')
		temp = list(Student.objects.filter(programme=programme, branch=branch))
		temp = [ i.name for i in temp ]
		return JsonResponse(temp,safe=False)

# Plays Caspar CG Animation
class PlayView(View):
	def post(self, request, *args, **kwargs):
		# Get POST data
		programme 	= request.POST.get('programme')
		branch 		= request.POST.get('branch')
		student 	= request.POST.get('student')
		# Modify them as needed
		name = student
		degree = programme + " " + branch
		# Play the CG
		cs = caspar.CasparServer('172.16.101.107', 5250)
		template_name = '20Convo/20CONVO'
		data = {'Sym1_Name':name, 'Sym1_Degree':degree}
		(req,res) = cs.cgplay(template_name,data)
		return HttpResponse(str(req) + "\n\n\n" + str(res))

		
# Stops running Caspar CG Animation
class StopView(View):
	def post(self, request, *args, **kwargs):
		cs = caspar.CasparServer('172.16.101.107', 5250)
		(req,res) = cs.cgstop()
		return HttpResponse(str(req) + "\n\n\n" + str(res))
		


