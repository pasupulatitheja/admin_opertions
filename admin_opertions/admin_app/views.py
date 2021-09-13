from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def showadminwelcome(request):
    uname = request.POST['uname']
    upass = request.POST['upass']
    if uname == 'admin' and upass == 'admin':
        request.session['name'] = uname
        return render(request,'badmin/adminwelcome.html')
    else:
        messages.error(request, "invalied Username/Password")
        return redirect('adminloginpage')
