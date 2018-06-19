from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from convo20.models import Student, VIP, Medal
from convo20.scripts import caspar
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model, authenticate, login, logout
# from django.contrib import messages
# import datetime
# from django.db import IntegrityError

# Create your views here.

class IndexView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		return render(request, 'convo20/index.html')

# Renders the student frontend page
class StudentView(LoginRequiredMixin, View):
	# Create a Caspar Server object
	def get(self, request, *args, **kwargs):
		global cs
		cs = caspar.CasparServer('172.16.101.107', 5250)
		# Render the index page
		temp = list(Student.objects.all())
		all_programmes  = set()
		all_branches    = set()
		for i in temp:
			all_programmes.add(i.programme)
			all_branches.add(i.branch)
		context = {
			'all_programmes' : all_programmes,
			'all_branches' : all_branches,
		}
		return render(request, 'convo20/student.html', context)

# Renders the VIP frontend page
class VIP_View(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		global cs
		cs = caspar.CasparServer('172.16.101.107', 5250)
		# Create a Caspar Server object
		#global cs
		#cs = caspar.CasparServer('172.16.101.107', 5250)
		
		# Render the index page
		temp = list(VIP.objects.all())
		all_VIPs = set()
		for i in temp:
			all_VIPs.add(i.name+", "+i.designation)
		context = {
			'all_VIPs' : all_VIPs,
		}
		return render(request, 'convo20/VIP.html', context)


# Renders the medal frontend page
class MedalView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		global cs
		cs = caspar.CasparServer('172.16.101.107', 5250)
		# Create a Caspar Server object
		#global cs
		#cs = caspar.CasparServer('172.16.101.107', 5250)
		
		# Render the index page
		temp = list(Medal.objects.all())
		all_medals = set()
		for i in temp:
			all_medals.add(i.name + ", " + i.programme + " (" + i.branch + ") ")
		context = {
			'all_medals' : all_medals,

		}
		return render(request, 'convo20/medal.html', context)


class UpdateView(LoginRequiredMixin, View):
	#def post_student(self, request, *args, **kwargs):
	def post(self, request, *args, **kwargs):
		programme 	= request.POST.get('programme')
		branch 		= request.POST.get('branch')
		temp = list(Student.objects.filter(programme=programme, branch=branch))
		temp = [ i.name for i in temp ]
		return JsonResponse(temp,safe=False)

	#Here no query is needed. also, I have to display name as well as designation in the form.... DO SOMETHING
	#def post_VIP(self, request, *args, **kwargs):
	#	temp = list(VIP.objects.all())
	#	temp = [ i.name+", "+i.designation for i in temp ]
	#	return JsonResponse(temp,safe=False)

	#Here no query is needed. also, I have to display name as well as everything else in the form.... DO SOMETHING
	#def post_medal(self, request, *args, **kwargs): 
	#	temp = list(Medal.objects.all())
	#	temp = [ i.name+", Winner: "+i.medal for i in temp ]
	#	return JsonResponse(temp,safe=False)


# Plays Caspar CG Animation
class PlayView(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		if request.POST.get('id') == "student":
			# Get POST data
			programme 	= request.POST.get('programme')
			branch 		= request.POST.get('branch')
			student 	= request.POST.get('student')
			# Modify them as needed
			name = student
			degree = programme + " " + branch
			degree = branch
			# Play the CG
			template_name = '20Convo/20CONVO'
			data = {'Sym1_Name':name, 'Sym1_Degree':degree}
			(req,res) = cs.cgplay(template_name,data)
			return HttpResponse(str(req) + "\n\n\n" + str(res))

		elif request.POST.get('id') == "vip":	
			#def post_VIP(self, request, *args, **kwargs):
			# Get POST data
			#designation 	= request.POST.get('designation')
			#return HttpResponse("Hi, Dafucks")
			name 	    = request.POST.get('VIP_name')
			#return HttpResponse(name)
			# Modify them as needed
			designation = VIP.objects.filter(name=name)[0].designation
			#return HttpResponse(name, designation)
			# Play the CG
			template_name = '20Convo/20CONVO'
			data = {'Sym1_Name':name, 'Sym1_Degree':designation}
			(req,res) = cs.cgplay(template_name,data)
			return HttpResponse(str(req) + "\n\n\n" + str(res))

		elif request.POST.get('id') == "medal":	
			#def post_medal(self, request, *args, **kwargs):
			# Get POST data
			#programme 	= request.POST.get('programme')
			#branch 		= request.POST.get('branch')
			medal_name  = request.POST.get('medal_name') 
			medal_instance = Medal.objects.filter(name=medal_name)[0]
			# Modify them as needed
			name   = medal_instance.name + ",  " + medal_instance.programme + " (" + medal_instance.branch + ") "
			degree = medal_instance.medal
			# Play the CG
			template_name = '20Convo/20CONVO'
			data = {'Sym1_Name':name, 'Sym1_Degree':degree}
			(req,res) = cs.cgplay(template_name, data)
			return HttpResponse(str(req) + "\n\n\n" + str(res))
		else:
			return HttpResponse("Hello! I don't know what is the problem.")


# Stops running Caspar CG Animation
class StopView(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		(req,res) = cs.cgstop()
		return HttpResponse(str(req) + "\n\n\n" + str(res))
		


