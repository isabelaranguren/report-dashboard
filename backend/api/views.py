from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle the uploaded file
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('File uploaded successfully')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    # Here, write the logic to handle the uploaded file.
    # For now, let's just save it to the server.
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
