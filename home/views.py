from django.shortcuts import render, HttpResponse
from home.models import Files
from home.Automation_ import ref_deteducation

def index(request):
    page = None
    document = None
    if request.method == 'POST' and request.FILES:
        document = request.FILES['upload']
        sve = Files(File_name=document)
        sve.save()
        content = {
            'data': ref_deteducation(document)
        }
        return render(request, "index.html", content)
    else:
        context = {'form': page, }
    return render(request, "index.html", context)


def login(request):

    return render(request, "auto.html", {'form': 1})



