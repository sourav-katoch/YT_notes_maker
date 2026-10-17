#program so far
import sys

def  get_youtube_link():
    youtube_url = input('Enter the YT link')
    print(youtube_url)

    if youtube_url.startswith('https://www.youtube.com') or youtube_url.startswith('www.youtube.com') or youtube_url.startswith('youtube.com') or youtube_url.startswith('https://youtu.be/') or youtube_url.startswith('youtu.be/'):
        pass
    else:
        sys.exit('Enter a valid YouTube URL')

    if youtube_url.startswith('https://youtu.be/') or youtube_url.startswith('youtu.be/'):
        if '?' in youtube_url:
            video_id = youtube_url[youtube_url.find('.be/')+4 : youtube_url.find('?') ]
        elif '?' not in youtube_url:
            video_id = youtube_url[youtube_url.find('.be/')+4 : ]
        
        else:
            sys.exit('Video could not be found. Please enter a valid Video URL')


    elif youtube_url.startswith('https://www.youtube.com') or youtube_url.startswith('www.youtube.com') or youtube_url.startswith('youtube.com'):
        if '=' not in youtube_url:
            sys.exit('Video could not be found. Please enter a valid Video URL')

        elif '=' in youtube_url and '&' in youtube_url:
            video_id = youtube_url[youtube_url.find('=')+1:youtube_url.find('&')]

        elif '=' in youtube_url and '&' not in youtube_url:
            video_id = youtube_url[youtube_url.find('=')+1: ]

    return video_id

video_id = get_youtube_link()
print(video_id)