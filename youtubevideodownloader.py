from pytube import YouTube

def download_youtube_video(url, resolution=None):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Print video details
        print("Title:", video.title)
        print("Thumbnail URL:", video.thumbnail_url)

        # List available streams
        videos = video.streams
        for i, stream in enumerate(videos):
            print(f"{i}. {stream}")

        # Choose a stream by resolution if specified
        if resolution is not None:
            selected_video = videos.filter(res=resolution).first()
        else:
            # If no resolution specified, let the user choose
            strm = int(input("Enter the stream number: "))
            selected_video = videos[strm]

        # Download the selected video
        selected_video.download()
        print("Download complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get YouTube video URL from user
    url = input("Enter YouTube video URL: ")

    # Optionally, specify resolution (e.g., '720p', '360p', etc.)
    resolution = input("Enter preferred resolution (press Enter to skip): ")

    # Download the YouTube video
    download_youtube_video(url, resolution)
