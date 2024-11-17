from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def home(req):
    
    if req.method == 'POST':
        name = req.POST.get("name")
        phone_no = req.POST.get("phone_no")
        
        newData = Contact(name=name,phone_no=phone_no)
        newData.save()
        
        return redirect('home-page')
    
    data = {}
    data['contacts'] = Contact.objects.all()
    return render(req,"index.html",data)

def delete_contact(request, contact_id):
    if request.method == 'POST':
        Contact.objects.filter(id=contact_id).delete()
        return redirect(home)