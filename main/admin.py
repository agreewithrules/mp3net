from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Song

# Register your models here.

admin.site.site_header = "Панель администрирования"

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    fields = ["name", "artist", "image", "preview", 
                        "audio", "audio_preview"]
    readonly_fields = ["preview", "audio_preview"]

    
    def preview(self, obj):
        return mark_safe(f"<img src={obj.image.url} style='max-width: 200px;'>")

    def audio_preview(self, obj):
        return mark_safe(f"<audio src={obj.audio.url} controls style='width: 500px;'></audio>")

    class Meta:
        model = Song
# admin.site.register(History)
