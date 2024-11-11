
class VideoService:

    def process_upload(self, video_id: int, chunk_index: int, chunk: bytes) -> None:
        pass

    def finalize_upload(self, video_id: int, total_chunks: int):
        pass
