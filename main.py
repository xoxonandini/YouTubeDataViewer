from src.youtube_api import get_channel_videos, get_video_stats
from src.utils import save_to_json

def main():
    # Replace these with your actual API key and channel ID
    const api_key = process.env.API_KEY;  # Replace with a valid YouTube Data API key
    channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Replace with a valid channel ID

    try:
        # Fetch videos from the specified channel
        videos = get_channel_videos(api_key, channel_id)
        
        if videos:
            video_data = []
            for video in videos:
                video_id = video['id']['videoId']  # This will now always exist
                stats = get_video_stats(api_key, video_id)
                
                # Build a dictionary of the video data
                video_info = {
                    'Title': video['snippet']['title'],
                    'Video ID': video_id,
                    'Views': stats.get('viewCount', 'N/A'),
                    'Likes': stats.get('likeCount', 'N/A'),
                    'Comments': stats.get('commentCount', 'N/A'),
                }
                video_data.append(video_info)

            save_to_json(video_data, 'data/video_data.json')
            print("Video data has been saved to 'data/video_data.json'.")
        else:
            print("No videos found for the specified channel.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
