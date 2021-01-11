from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):

		return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST.get('message_email')
		
		

		return render(request, 'contact.html', {'message_name' : message_name, 'message_email' : message_email})

	else:
		return render(request, 'contact.html', {})

'''		email = request.POST['email']
		comments = request.POST['comments']
send_mail(
			message_name,
			message_email,
			['aditya.kr.m2@gmail.com'],
			)
		'''