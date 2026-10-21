#program so far
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()

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

# implement get transcript from the video usinmg api https://www.youtube.com/watch?v=XZnuIIcc8VY
ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)
print(fetched_transcript)
final_transcript = ''
for snippet in fetched_transcript.snippets:
 final_transcript += ''.join(snippet.text)

# function to call api and create notes
def generate_notes(transcript):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents = f"""
        Create structured study notes from the transcript below.

        Include:
        1. A concise overview
        2. Topic-wise notes with headings
        3. Important concepts and examples mentioned
        4. Key takeaways
        5. A short summary

        Accuracy rules:
        - Use only information supported by the transcript.
        - Do not invent facts, examples, statistics, or quotes.
        - If something is unclear in the transcript, say so.
        - Remove unnecessary repetition.

        TRANSCRIPT:
        {transcript}
        """
    )
    return response.text
notes = generate_notes(final_transcript)

os.makedirs("notes", exists_ok=True)

filename = f'notes-{video_id}.md'
with open('notes.md', 'w', encoding='utf-8') as file:
    file.write(notes)
print(f"Notes saved to {filename}")

#implement file saving logic so it does not get overwritten

    