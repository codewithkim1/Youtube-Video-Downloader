import os
import pytest
from pytube import YouTube
from main import download_video

def test_download_video():
    # Define test URL and directory
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    dir = './test_dir'
    
    # Download the video
    download_video(url, dir)
    
    # Check that the video was downloaded to the specified directory
    assert os.path.exists(os.path.join(dir, 'Rick Astley - Never Gonna Give You Up (Video).mp4'))
    
    # Check that the video is not corrupted
    with open(os.path.join(dir, 'Rick Astley - Never Gonna Give You Up (Video).mp4'), 'rb') as f:
        assert f.read(4) == b'\x00\x00\x00\x18' # MP4 file header
    
    # Clean up by deleting the downloaded file
    os.remove(os.path.join(dir, 'Rick Astley - Never Gonna Give You Up (Video).mp4'))
