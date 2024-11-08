from django.contrib import admin
from django.contrib.auth.admin import csrf_protect_m
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import path, reverse
from django.utils.html import format_html

from core.forms import VideoChunkFinishUploadForm
from core.models import Video, Tag
from core.services import VideoService


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'is_published', 'num_likes', 'num_views', 'redirect_to_upload',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
			path('<int:id>/upload-video', self.upload_video, name='core_video_upload')
		]
        return custom_urls + urls

    def redirect_to_upload(self, obj: Video):
        url = reverse('admin:core_video_upload', args=[obj.id])
        return format_html(f'<a href="{url}">Upload</a>')

    redirect_to_upload.short_description = 'upload'

    @csrf_protect_m
    def upload_video(self, request, id):

        if request.method == 'POST':
            form = VideoChunkFinishUploadForm(request.POST, request.FILES)

            if not form.is_valid():
                return JsonResponse({"error": form.errors}, status=400)

            VideoService().process_upload(
				video_id=id,
				chunk_index=form.cleaned_data['chunkIndex'],
                chunk=form.cleaned_data['chunk'].read()
			)

        return render(request, 'admin/core/upload_video.html')

# Register your models here.
admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
