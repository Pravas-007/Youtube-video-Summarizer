from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

def get_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return None

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([x['text'] for x in transcript])
    return full_text

def summarize_text(text):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    chunks = [text[i:i+1024] for i in range(0, len(text), 1024)]
    summary = ""

    for chunk in chunks:
        result = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "

    return summary.strip()

video_url = input("🎥 Enter YouTube Video URL: ")
video_id = get_video_id(video_url)

if not video_id:
    print("❌ Invalid YouTube URL")
else:
    print("📜 Fetching transcript...")
    try:
        transcript = get_transcript(video_id)
        print("🧠 Summarizing...")
        summary = summarize_text(transcript)
        print("\n✅ Summary:\n")
        print(summary)
    except Exception as e:
        print(f"❌ Error: {e}")

# This script fetches the transcript of a YouTube video and summarizes it using a pre-trained model.
