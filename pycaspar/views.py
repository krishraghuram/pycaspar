from django.http import HttpResponseRedirect
from django.urls import reverse

def redirect(request, url_name):
	return HttpResponseRedirect(reverse(url_name))