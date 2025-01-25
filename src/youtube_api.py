from googleapiclient.discovery import build

def get_channel_videos(api_key, channel_id):
    """
    Fetches the videos from a given YouTube channel.
    
    :param api_key: Your YouTube Data API key.
    :param channel_id: The ID of the YouTube channel.
    :return: A list of videos in the channel.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50
    )
    response = request.execute()

    # Filter videos only (items where id.kind == 'youtube#video')
    videos = [item for item in response['items'] if item['id']['kind'] == 'youtube#video']
    return videos

def get_video_stats(api_key, video_id):
    """
    Fetches statistics for a given YouTube video.
    
    :param api_key: Your YouTube Data API key.
    :param video_id: The ID of the YouTube video.
    :return: A dictionary with view count, like count, and comment count.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()

    # Extract the video stats
    stats = response['items'][0]['statistics']
    return stats
