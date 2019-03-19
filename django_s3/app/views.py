from django.shortcuts import render
from .forms import *
from django.core.files.storage import FileSystemStorage


def index(request):
	if request.method == 'POST':
		print('Request: ', request.FILES)

		myfile = request.FILES
		print('File:', myfile)
		form = CustomerForm(request.POST, myfile)

		if form.is_valid():
			form.save()
	else:
		form = CustomerForm()


	context = {'form':form}
	return render(request, 'app/index.html', context)