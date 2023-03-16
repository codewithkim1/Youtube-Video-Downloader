from pytube import YouTube

# Ask the user to input the URL of the YouTube video
url = input('Enter the URL of the YouTube video: ')

# Create a YouTube object from the URL
yt = YouTube(url)

# Get the first stream (usually the highest quality)
stream = yt.streams.first()

# Ask the user to input the directory to save the video
dir = input('Enter the directory to save the video (leave blank for current directory): ')

if dir:
    # Download the stream to the specified directory
    stream.download(dir)
else:
    # Download the stream to the current working directory
    stream.download()
