from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def submit(request):
    if request.method == 'POST':
        em =request.POST.get('email')
        sub=request.POST.get('sub')
        mess = request.POST.get('mess')
        sender="tejaswinipatil95355@gmail.com"
        send_mail(
            sub,
            mess,
            sender,
            [em],
            fail_silently=False,
        )
        context={}
        context['success']="Email Send Successfully!"
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')



