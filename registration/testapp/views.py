from django.shortcuts import render
from testapp.forms import loginForm

# Create your views here.
def create(request):
    form_class=loginForm
    form=form_class() 
    if request.method=='POST':
        form=form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'index.html')

    else:

        return render(request,'index.html',{'form':form})