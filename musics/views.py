from django.shortcuts import render

from .models import Album

# Create your views here.


def musics(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'musics/index.html', context)


def dashboards(request):
    albums = Album.objects.all()
    context = {'albums': albums}
    return render(request, 'musics/dashboard.html', context)

# def songs(request):
#     song = serializers.serialize('json', Song.objects.all())
#     return HttpResponse(song, content_type="application/json")
# def albums(request):
#     album = serializers.serialize('json', Album.objects.all())
#     return HttpResponse(album, content_type="application/json")
# def organizations(request):
#     organization = serializers.serialize('json', Organization.objects.all())
#     return HttpResponse(organization, content_type="application/json")
