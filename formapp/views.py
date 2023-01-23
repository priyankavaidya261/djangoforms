from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']																																							
			email = form.cleaned_data['email']	
			print(name,email)		



	form =  ContactForm()
	return render(request,'form.html',{'form':form})

def home(request):
	home = request.POST['name']
	home_k = request.POST['email']
	Hello = home + home_k
	return render(request,'home.html',{'Hello':Hello})
