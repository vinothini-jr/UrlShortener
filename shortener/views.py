from django.shortcuts import render,redirect,HttpResponse
from .forms import DataForm
from .models import Data
import uuid
# Create your views here.

def home(request):
    form = DataForm()
    return render(request,'shortener/home.html',{'form':form})

def process(request):
    if request.method == 'POST':
        link=request.POST['link']
        link_id=str(uuid.uuid4())[:5]
        new_link=Data(link=link,uuid=link_id)
        new_link.save()
        link_id = "http://127.0.0.1:8000/" + link_id
        context={
            'link_id':link_id,
        }
        return render(request,'shortener/process.html',context)
def redirecturl(request,uuid):
    try:
       new_link=Data.objects.get(uuid=uuid)
    except Data.DoesNotExist:
        new_link=None
    if new_link is not None:
        return redirect(new_link.link)
    else:
        return HttpResponse("wrong url")