from core.models import Video, VideoMedia

class VideoService:

    def get_chunk_directory(self, video_id: int) -> str:
        return f'/tmp/videos/{video_id}'

    def find_video(self, video_id: int) -> Video:
        return Video.objects.get(id=video_id)

    def process_upload(self, video_id: int, chunk_index: int, chunk: bytes) -> None:
        pass

    def finalize_upload(self, video_id: int, total_chunks: int):
        pass
