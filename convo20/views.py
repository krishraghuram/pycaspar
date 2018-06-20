import socket
import threading
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from convo20.models import Student, Dignitary, Medal
from convo20.scripts import caspar



def setup_caspar():
	# If it does not exist, setup Caspar CG Server
	ip = '172.16.101.107'
	port = 5250
	global cs
	try:
		if cs is None:
			cs = caspar.CasparServer(ip,port)
		else:
			pass
	except socket.timeout:
					pass # Send error message
	except socket.error:
					pass # Send error message			
	except NameError:
			try:
				cs = caspar.CasparServer(ip,port)
			except socket.timeout:
					pass # Send error message
			except socket.error:
					pass # Send error message
	# Clear all running CG
	try:
		t = threading.Thread(target=cs.cgstop)
		t.start()
	except:
		pass

# Create your views here.

# Renders main page
class IndexView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		# Setup CasparCG
		setup_caspar()
		# Render the main page
		return render(request, 'convo20/index.html')

# Renders the Student page
class StudentView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		# Setup CasparCG
		setup_caspar()
		# Render the Student page
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

# Renders the Dignitary page
class DignitaryView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		# Setup CasparCG
		setup_caspar()
		# Render the Dignitary page
		all_dignitaries = list(Dignitary.objects.all())
		all_dignitaries = [ {'name':i.name,'id':i.id} for i in all_dignitaries ]
		context = {
			'all_dignitaries' : all_dignitaries,
		}
		return render(request, 'convo20/dignitary.html', context)

# Renders the Medal page
class MedalView(LoginRequiredMixin, View):
	def get(self, request, *args, **kwargs):
		# Setup CasparCG
		setup_caspar()
		# Render the index page
		all_medal_winners = list(Medal.objects.all())
		all_medal_winners = [ {'name':i.name,'id':i.id} for i in all_medal_winners ]
		context = {
			'all_medal_winners' : all_medal_winners,
		}
		return render(request, 'convo20/medal.html', context)

# Update's list of students based on programme and branch
class UpdateView(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		# Get POST data
		programme 	= request.POST.get('programme')
		branch 	= request.POST.get('branch')
		temp = list(Student.objects.filter(programme=programme, branch=branch))
		temp = [ {'name':i.name,'id':i.id} for i in temp ]
		return JsonResponse(temp,safe=False)

# Plays Caspar CG Animation
class PlayView(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		# Get POST data
		pk = request.POST.get('id')
		referer = request.POST.get('referer')
		# Get the instance from DB
		if referer == reverse('convo20:dignitary'):
			instance = Dignitary.objects.get(pk=pk)
			name = instance.name
			degree = instance.designation
		elif referer == reverse('convo20:medal'):
			instance = Medal.objects.get(pk=pk)
			name = instance.name
			degree = instance.medal
		elif referer == reverse('convo20:student'):
			instance = Student.objects.get(pk=pk)
			name = instance.name
			degree = instance.programme + " " + instance.branch
		else:
			return HttpResponse("From PlayView : Bad Referer")
		# Play the CG
		template_name = '20Convo/20CONVO'
		data = {'Sym1_Name':name, 'Sym1_Degree':degree}
		(req,res) = cs.cgplay(template_name,data)
		return HttpResponse(str(req) + "\n\n\n" + str(res))



# Stops running Caspar CG Animation
class StopView(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		(req,res) = cs.cgstop()
		return HttpResponse(str(req) + "\n\n\n" + str(res))
		

