from django.shortcuts import render, get_object_or_404
from .models import Image
# Create your views here.
def gallery(request) :
    images = Image.objects
    return render(request, 'gallery.html', {'images': images})

def imageDetail(request, image_id):
    imageDetails = get_object_or_404(Image, pk = image_id)
    return render(request, 'imageDetail.html', {'imageDetails' : imageDetails})