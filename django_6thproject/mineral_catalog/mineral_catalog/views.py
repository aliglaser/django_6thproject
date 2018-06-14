from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def hello_world(request):
	return HttpResponse("herro")