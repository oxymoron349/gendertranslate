from django.shortcuts import render
from django.http import HttpResponse
from .genderize import genderize

# Create your views here.

def home_page(request):
	if request.method == 'GET':
		text_output = ""
	elif request.method == 'POST':
		text_output = genderize(request.POST.get('text', ''))


	render_variables = {'text_input': request.POST.get('text', 'Text hier einfügen.'), 'text_output': text_output}
	return render(request, 'home.html', render_variables)

