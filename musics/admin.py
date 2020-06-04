from django.contrib import admin

from .models import Song

from .models import Album

from .models import Organization

# Register your models here.

admin.site.register(Song)

admin.site.register(Album)

admin.site.register(Organization)
