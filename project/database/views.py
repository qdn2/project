# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django import template
from django.template.loader import get_template 
from database.models import Question

def search(request):
    template = get_template('search.html')
    context = {
    }
    return HttpResponse(template.render(context, request))



def results(request):
	query = request.GET['q']
	template = get_template('results.html')

	try:
		results=Question.objects.filter(question_text= query)
		context = { 'results': results}
	except Question.DoesNotExist:
		results="wrong"
		context = { 'results': results}	

	return HttpResponse(template.render(context,request))
